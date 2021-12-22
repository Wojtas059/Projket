from _typeshed import Self
from User.user import User
from enum import Enum
import re
from crypto.securityCreator import SecurityCreator

from database.database_handler import DatabaseHandler


class UserValidator():

    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'

    class Flags(Enum):
        INCORRECTNAME = 1
        INCORRECTSURNAME = 2
        INCORRECTPASSWORD = 3
        INCORRECTUSERPASSWORD = 4
        INCORRECTLOGIN = 5
        INCORRECTELOGINDUPLICATE = 6
        INCORRECTEMAIL = 7
        INCORRECTEMAILDUPLICATE = 8
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
        databaseHandler = DatabaseHandler
        databaseHandler.createConnection()
        if databaseHandler.findAnyEmail(self.user.email):
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

    def validateUserPassword(self):
         if SecurityCreator.verifyPassword(self.user):
             return self.Flags.CORRECTFIELD
         else:
             return self.Flags.INCORRECTUSERPASSWORD
         
    def validateLogin(self):
        if len(self.user.name) > 3:
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTLOGIN

    def validateUserLogin(self):
        databaseHandler = DatabaseHandler
        databaseHandler.createConnection()
        if databaseHandler.findAnyLogin(self.user.login):
            databaseHandler.closeConnection()
            return self.Flags.CORRECTFIELD
        else:
            databaseHandler.closeConnection()
            return self.Flags.INCORRECTLOGIN

    def validateLoginExistence(self):
        databaseHandler = DatabaseHandler
        databaseHandler.createConnection()
        if databaseHandler.findAnyEmail(self.user.login):
            databaseHandler.closeConnection()
            return self.Flags.CORRECTFIELD
        else:
            databaseHandler.closeConnection()
            return self.Flags.INCORRECTELOGINDUPLICATE

    def validateRegistrations(self):
        validationResults = {}
        validationResults["NAME"] = self.validateName()
        validationResults["SURNAME"] = self.validateSurname()
        validationResults["PASSWORD"] = self.validatePassword()
        validationResults["LOGIN"] = self.validateLogin()
        validationResults["LOGINEXISTENCE"] = self.validateLoginExistence()
        validationResults["EMAIL"] = self.validateEmail()
        validationResults["EMAILEXISTENCE"] = self.validateEmailExistence()
        return validationResults

    def validateLogin(self):
        validationResults = {}
        validationResults["USERLOGIN"]=self.validateUserLogin()
        if validationResults["USERLOGIN"]==self.Flags.CORRECTFIELD:
            validationResults["USERPASSWORD"]=self.validatePassword()
        else:
            validationResults["USERPASSWORD"]=self.Flags.INCORRECTUSERPASSWORD
        return validationResults