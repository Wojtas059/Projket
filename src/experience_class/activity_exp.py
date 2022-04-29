class ActivityExperience:
    def __init__(self, **kwargs):
        self.type_activity: str = kwargs.get('type_activity', "")
        self.type_exercise: str = kwargs.get('type_exercise', "")
        self.type_physique: str = kwargs.get('type_physique', "")
        self.humidity: str = kwargs.get('humidity', "")

    # Getter and Setter method 
    def setTypeActivity(self, type_activity: str):
        self.type_activity = type_activity
    
    def getTypeActivity(self)->str:
        return self.type_activity

    def setTypeExperience(self, type_exercise: str):
        self.type_exercise = type_exercise
    
    def getTypeExperience(self)->str:
        return self.type_exercise

    def setTypePhysique(self, type_physique: str):
        self.type_physique = type_physique
    
    def getTypePhysique(self)->str:
        return self.type_physique

    def setHumidity(self, humidity: str):
        self.humidity = humidity
    
    def getHumidity(self)->str:
        return self.humidity
