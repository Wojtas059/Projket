class Measurement():
    # Powyższa klasa odpowiada za przechowywanie danych, które odpowiadaja 
    # konfiguracji pomiarowej przez użytkownika 
    def __init__(self) -> None:
        self.type = ""
        self.many = 0
        self.data_muscular = []
        self.men = {}

    #Dwie funckje geter i setter odpowiadaja za zmienną type czli Auto lub Manual
    def get_type(self):
        return self.type
    
    def set_type(self, type_):
        self.type = type_


    #Dwie funckje geter i setter odpowiadaja liczbę badanych mięsni
    def get_many_sensor(self):
        return self.namy
    
    def set_many_sensor(self, many_):
        self.namy = many_


    #Cztery funckje (dwie)geter i (dwie)setter odpowiadaja za zmienną typu lista,
    # która przetrzymuje dane odpowiadające wybranych partii mięśni przez użytkownika
    def get_data_muscular(self):
        return self.data_muscular
    
    def get_data_muscular_index(self, index):
        return self.data_muscular[index]

    def set_data(self, data):
        self.data_muscular = data

    def add_data(self, data):
        self.data_muscular.append(data)



    def get_men(self):
        return self.men
    
    def get_men_keys(self, keys):
        return self.men[keys]

    def set_men(self, data):
        self.men = data
    
    def add_men(self,index, data):
        self.men[index] = data

    #def add_men_index(self, index, data):
    #    self.men[index].append(data)


    