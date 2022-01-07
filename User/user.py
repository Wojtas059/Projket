
class User():
    def  __init__(self,login:str,password:str,name:str="",surname:str="",email:str="",advanced_user_key="",advanced:int=0):
        self.id_user=0
        self.name=name
        self.surname=surname
        self.password=password
        self.login=login
        self.email=email
        self.advanced_user_key=advanced_user_key
        self.advanced=advanced

    
