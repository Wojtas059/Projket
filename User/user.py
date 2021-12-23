
class User():
    def  __init__(self,login:str,password:str,name:str="",surname:str="",email:str="",advanced:int=0):
        self.id_user=0
        self.name=name
        self.surname=surname
        self.password=password
        self.login=login
        self.email=email
        self.advanced=advanced
