# Prototyp aplikacji do predykcji szeregow czasowych w trybie diagnostycznym dla danych pilotazowych
import time
import timeit
import psutil 

def init(): # *** Inicjalizacja ***
    print("\033[2J") # Czyszczenie okna konsoli    
    global cv2, os, sys, glob, pd, pickle, tsfresh, m, plt, extract_features, FILE_LIST, \
    MODE, COLUMN_NAMES, MODEL, MODEL_LIST, DIR_RES, MEANS, VARIANCES, PREDICTION
    import cv2, os, sys, glob, pickle, tsfresh
    import pandas as pd
    import math as m
    import matplotlib.pyplot as plt
    from tsfresh import extract_features            
    DIR_MOD = 'models' # Katalog z plikami modeli
    MODEL_LIST = glob.glob(DIR_MOD + '/*')                          
    DIR_SER = 'series' # Katalog z plikami szeregow czasowych
    FILE_LIST = glob.glob(DIR_SER + '/*')                          
    base_dir = './'
    DIR_RES = os.path.join(base_dir, 'results') # Katalog z wynikami predykcji
    if not os.path.exists(DIR_RES) :
        os.mkdir(DIR_RES)    
    COLUMN_NAMES = ['EMG__sum_values', 'EMG__standard_deviation', 'MMG__sum_values', 'MMG__standard_deviation']    
    MEANS = pd.read_csv('normal/means.csv', header=None, sep=';', decimal='.')
    MEANS = MEANS.T
    VARIANCES = pd.read_csv('normal/variances.csv', header=None, sep=';', decimal='.')
    VARIANCES = VARIANCES.T    
    if len(MODEL_LIST) > 0:        
        MODEL = pickle.load(open(MODEL_LIST[0], 'rb'))            
    else:
        raise('\nNo models available!')

def dataOnline(df): # Do implementacji w trybie online  
    df['EMG'] 
    df['MMG'] 
    formatData()                
    extractFeatures()                
    rescaleFeatures()        
    setColumns()                        
    makeClassification()    
    
def dataOffline(): # Petla dzialajaca w trybie diagnostycznym
    global df, N, time, FILE_PATH    
    if len(FILE_LIST) > 0:        
        for FILE_PATH in FILE_LIST:                                    
            t1 = cv2.getTickCount()
            df_temp = pd.read_csv(FILE_PATH, header=None, sep=';', decimal='.')                                 
            (N, _) = df_temp.shape # N - liczba probek szeregu czasowego         
            df = pd.DataFrame()
            df['EMG'] = df_temp[0]
            df['MMG'] = df_temp[1]                                                
            # *** Funkcje wspolne dla obu trybow pracy ***
            formatData() 
            extractFeatures()                
            rescaleFeatures()        
            setColumns()                        
            makeClassification()
            # ********************************************
            t2 = cv2.getTickCount()
            time = (t2-t1)/cv2.getTickFrequency()                
            drawGraphs()            
    else:
        print('\nNo time series for prediction!')
        sys.exit(0)
    
def loadData():
    global df, MODE  
    if MODE == 'ONLINE MODE':
        dataOnline()        
    else:
        dataOffline()
    
def formatData(): # Formatowanie danych     
    global df
    df['id'] = 1
    df['time'] = range(0, N)
    HEADER_LIST = ['id', 'time', 'EMG', 'MMG'] # Struktura wymagana przez modul ekstrakcji cech tsfresh
    df = df.reindex(columns = HEADER_LIST)         

def extractFeatures(): # Ekstrakcja cech istotnych    
    global X    
    RELEVANT_FEATURES = tsfresh.feature_extraction.settings.from_columns(columns = COLUMN_NAMES)
    X = extract_features(df, column_id = 'id', column_sort = 'time', kind_to_fc_parameters = RELEVANT_FEATURES)
    X.to_numpy()        

def rescaleFeatures(): # Przeskalowanie cech z wykorzystaniem srednich i wariancji
    (ROWS, COLS) = X.shape    
    for i in range(0, COLS):
        X.iloc[0,i] = (X.iloc[0, i] - MEANS.iloc[0, i]) / m.sqrt(VARIANCES.iloc[0, i])

def setColumns(): # Ustalenie kolejnosci cech wedlug ich rankingu    
    global X    
    HEADER_LIST = ['MMG__standard_deviation', 'EMG__sum_values', 'EMG__standard_deviation', 'MMG__sum_values']
    X = X.reindex(columns = HEADER_LIST)
    # Zastapienie nazw cech ich aliasami
    X.rename(columns = {'MMG__standard_deviation': 'X15', 
                        'EMG__sum_values': 'X1',
                        'EMG__standard_deviation': 'X5',
                        'MMG__sum_values': 'X11'}, inplace=True)

def makeClassification(): # Klasyfikacja
    global CLASS_LABEL, PROB, TAK, NIE
    PREDICTION = MODEL.predict(X) # Funkcja predict() zwraca etykiete klasy    
    if PREDICTION[0] == 'NIETRENUJĄCY':
        CLASS_LABEL = 'NON-TRAINING'
    else:
        CLASS_LABEL = 'TRAINING'
    PROB = MODEL.predict_proba(X) # Funkcja predict_proba() zwraca prawdopodobienstwo przynaleznosci do klasy 

def drawGraphs(): # Rysowanie wykresow z danymi diagnostycznymi
    fig, (ax1, ax2) = plt.subplots(nrows = 2, ncols = 1, sharex = True, sharey = False, figsize = (12, 6))
    ax1.plot(df['EMG'], color='red')        
    ax1.set_title('Electromyographic signal (EMG)')
    ax1.set_ylabel(u"$U_{RMS}$ [\u03bcV]")    
    ax1.grid(True)
    
    ax2.plot(df['MMG'], color='blue')                              
    ax2.set_title('Mechanomyographic signal (MMG)')
    ax2.set_ylabel('$U_{RMS}$ [mV]')        
    ax2.set_xlabel('Sample number')        
    ax2.grid(True)        
    
    FILE_NAME = os.path.splitext(os.path.basename(FILE_PATH))[0]
    MODEL_NAME = os.path.splitext(os.path.basename(MODEL_LIST[0]))[0]
    fig.suptitle('Model: ' + MODEL_NAME +
                 '\nTime series: ' + FILE_NAME + '\nDiagnosis: ' + CLASS_LABEL +
                 '\nProbability: TRAINING \u2212 ' + str(round(PROB[0,1], 4)) +
                 ', NON-TRAINING \u2212 ' + str(round(PROB[0,0], 4)) +
                 '\nProcessing time: ' + str(round(time, 3)) + ' seconds')
    fig.tight_layout(pad = 2)
    fig.savefig(DIR_RES + '/' + FILE_NAME + '.png', dpi = 125)         

def main():                        
    init()
    modeSelection()
    loadData()          
        
if __name__ == '__main__':
    main()
    

