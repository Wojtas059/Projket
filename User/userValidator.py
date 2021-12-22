from _typeshed import Self
from repo.User.user import User
from enum import Enum
import re

from repo.database.database_handler import DatabaseHandler


class UserValidator():

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    class Flags(Enum):
        INCORRECTNAME = 1
        INCORRECTSURNAME = 2
        INCORRECTPASSWORD = 3
        INCORRECTLOGIN = 4
        INCORRECTELOGINDUPLICATE = 5
        INCORRECTEMAIL = 6
        INCORRECTEMAILDUPLICATE = 7
        CORRECTFIELD = 0

    def __init__(self, user: User):
        self.user = user

    def validateName(self):
        if len(self.user.name) > 3:
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTNAME

    def validateSurname(self):
        if len(self.user.surname) > 3:
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTSURNAME

    def validateEmail(self):
        if re.fullmatch(self.regex, self.user.email):
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTEMAIL

    def validateEmailExistence(self):
        databaseHandler= DatabaseHandler
        databaseHandler.createConnection()
        if  databaseHandler.findAnyEmail(self.user.email):
            databaseHandler.closeConnection()
            return self.Flags.CORRECTFIELD
        else:
            databaseHandler.closeConnection()
            return self.Flags.INCORRECTEMAILDUPLICATE
    def validatePassword(self):
        if len(self.user.password) > 8:
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTPASSWORD

    def validateLogin(self):
        if len(self.user.name) > 3:
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTLOGIN
    
    def validateLoginExistence(self):
        databaseHandler= DatabaseHandler
        databaseHandler.createConnection()
        if  databaseHandler.findAnyEmail(self.user.login):
            databaseHandler.closeConnection()
            return self.Flags.CORRECTFIELD
        else:
            databaseHandler.closeConnection()
            return self.Flags.INCORRECTELOGINDUPLICATE

    def validate(self):
        validationResults= {}
        validationResults["NAME"]=self.validateName()
        validationResults["SURNAME"]=self.validateSurname()
        validationResults["PASSWORD"]=self.validatePassword()
        validationResults["LOGIN"]=self.validateLogin()
        validationResults["LOGINEXISTENCE"]=self.validateLoginExistence()
        validationResults["EMAIL"]=self.validateEmail()
        validationResults["EMAILEXISTENCE"]=self.validateEmailExistence()
        return  validationResults
