import logging
from multiprocessing import Process
import multiprocessing
import cv2, os, sys, glob, pickle, tsfresh
import pandas  as pd
import math as m 
import matplotlib.pyplot as plt
from tsfresh import extract_features    

# global cv2, os, sys, glob, pd, pickle, tsfresh, m, plt, extract_features, FILE_LIST, \
#         MODE, COLUMN_NAMES, MODEL, MODEL_LIST, DIR_RES, MEANS, VARIANCES, PREDICTION



class Prediction(Process):
    DIR_MOD = 'models' # Katalog z plikami modeli
    DIR_SER = 'series' # Katalog z plikami szeregow czasowych
    base_dir = './'
    result = {}
    def __init__(self, df:pd.DataFrame,queue_result):
        super(Prediction,self).__init__()
        self.df=df
        self.queue_result=queue_result
        self.MODEL_LIST = glob.glob(self.DIR_MOD + '/*')                          
        self.FILE_LIST = glob.glob(self.DIR_SER + '/*')                          
        self.DIR_RES = os.path.join(self.base_dir, 'results') # Katalog z wynikami predykcji
        if not os.path.exists(self.DIR_RES) :
            os.mkdir(self.DIR_RES)    
        self.COLUMN_NAMES = ['EMG__sum_values', 'EMG__standard_deviation', 'MMG__sum_values', 'MMG__standard_deviation']   
        self.MEANS = pd.read_csv('normal/means.csv', header=None, sep=';', decimal='.')
        self.MEANS = self.MEANS.T
        self.VARIANCES = pd.read_csv('normal/variances.csv', header=None, sep=';', decimal='.')
        self.VARIANCES = self.VARIANCES.T    
        if len(self.MODEL_LIST) > 0:        
            self.MODEL = pickle.load(open(self.MODEL_LIST[0], 'rb'))            
        else:
            raise('\nNo models available!')

    def formatData(self): # Formatowanie danych     
        (N, _) = self.df.shape # N - liczba probek szeregu czasowego 
        self.df['id'] = 1
        self.df['time'] = range(0, N)
        HEADER_LIST = ['id', 'time', 'EMG', 'MMG'] # Struktura wymagana przez modul ekstrakcji cech tsfresh
        self.df = self.df.reindex(columns = HEADER_LIST)    

    def extractFeatures(self): # Ekstrakcja cech istotnych    
        self.RELEVANT_FEATURES = tsfresh.feature_extraction.settings.from_columns(columns = self.COLUMN_NAMES)
        print(self)
        self.X = extract_features(self.df, column_id = 'id', column_sort = 'time', kind_to_fc_parameters = self.RELEVANT_FEATURES)
        self.X.to_numpy()   

    def rescaleFeatures(self): # Przeskalowanie cech z wykorzystaniem srednich i wariancji
        (ROWS, COLS) = self.X.shape    
        for i in range(0, COLS):
            self.X.iloc[0,i] = (self.X.iloc[0, i] - self.MEANS.iloc[0, i]) / m.sqrt(self.VARIANCES.iloc[0, i])

    def setColumns(self): # Ustalenie kolejnosci cech wedlug ich rankingu    
        HEADER_LIST = ['MMG__standard_deviation', 'EMG__sum_values', 'EMG__standard_deviation', 'MMG__sum_values']
        self.X = self.X.reindex(columns = HEADER_LIST)
        # Zastapienie nazw cech ich aliasami
        self.X.rename(columns = {'MMG__standard_deviation': 'X15', 
                            'EMG__sum_values': 'X1',
                            'EMG__standard_deviation': 'X5',
                            'MMG__sum_values': 'X11'}, inplace=True)
    def makeClassification(self): # Klasyfikacja
        self.PREDICTION = self.MODEL.predict(self.X) # Funkcja predict() zwraca etykiete klasy    
        if self.PREDICTION[0] == 'NIETRENUJĄCY':
            self.CLASS_LABEL = 'NON-TRAINING'
        else:
            self.CLASS_LABEL = 'TRAINING'
        self.PROB = self.MODEL.predict_proba(self.X) # Funkcja predict_proba() zwraca prawdopodobienstwo przynaleznosci do klasy 
        self.result = {self.CLASS_LABEL:self.PROB} 
    def launch_prediction(self):
        self.formatData()
        self.extractFeatures()                
        self.rescaleFeatures()        
        self.setColumns()                        
        self.makeClassification()   
        self.queue_result.put(self.result)
    def run(self):
        
        self.launch_prediction()