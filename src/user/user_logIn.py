class UserLogIn:
    def __init__(self, id: str,login:str, name: str, surname: str, email: str):
        self.id_user = id
        self.login = login
        self.email_user = email
        self.name_user = name
        self.surname_user = surname

    def get_id(self):
        return self.id_user
    
    def get_login(self):
        return self.login

    def get_email(self):
        return self.email_user

    def get_name(self):
        return self.name_user

    def get_surname(self):
        return self.surname_user
