
class User():
    def  __init__(self,name:str,surname:str,password:str,login:str,email:str,advanced:int):
        self.id_user=0
        self.name=name
        self.surname=surname
        self.password=password
        self.login=login
        self.email=email
        self.advanced=advanced

    #def  __init__(self,password:str,login:str):
    #    self.id_user=0
    #    self.password=password
    #    self.login=login