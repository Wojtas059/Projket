#  The class is responsible for storing the data of log in user

class UserLogIn:
    def __init__(self, **kwargs):
        self.id_user = kwargs.get('id', "")
        self.name_user =  kwargs.get('name', "")
        self.surname_user =  kwargs.get('surname', "")
        self.login_user =  kwargs.get('login', "")
        self.email_user =  kwargs.get('email', "")
        self.advanced_user = kwargs.get('advanced', False)

    def get_id(self):
        return self.id_user
    
    def set_id(self, id_user):
        self.id_user = id_user

    def get_name(self):
        return self.name_user

    def set_name(self, name_user):
        self.name_user = name_user

    def get_surname(self):
        return self.surname_user

    def set_surname(self, surname_user):
        self.surname_user = surname_user

    def get_login(self):
        return self.login_user

    def set_login(self, login_user):
        self.login_user = login_user

    def get_email(self):
        return self.email_user
        
    def set_email(self, email_user):
        self.email_user = email_user
    
    def get_advanced(self):
        return self.advanced_user
    
    def set_advanced(self, advanced_user):
        self.advanced_user = advanced_user
    



