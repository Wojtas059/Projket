import re
from enum import Enum

from src.crypto.securityCreator import SecurityCreator
from src.database_handlers.database_handler import DatabaseHandler
from src.user.user import User


class UserValidator:

    # TODO fix name for email regex
    regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"

    class Flags(Enum):
        INCORRECTNAME = 1
        INCORRECTSURNAME = 2
        INCORRECTPASSWORD = 3
        INCORRECTUSERPASSWORD = 4
        INCORRECTLOGIN = 5
        INCORRECTELOGINDUPLICATE = 6
        INCORRECTEMAIL = 7
        INCORRECTEMAILDUPLICATE = 8
        NONEXISTENTADVANCEDUSERKEY = 9
        CORRECTFIELD = 0

    def __init__(self, user: User):
        self.user = user

    def validateName(self):
        if len(self.user.name) > 2:
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTNAME

    def validateSurname(self):
        if len(self.user.surname) > 2:
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTSURNAME

    def validateEmail(self):
        if re.fullmatch(self.regex, self.user.email):
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTEMAIL

    def validateEmailExistence(self):
        databaseHandler = DatabaseHandler()
        databaseHandler.createConnection()
        if databaseHandler.findAnyEmail(self.user.email):
            databaseHandler.closeConnection()
            return self.Flags.CORRECTFIELD
        else:
            databaseHandler.closeConnection()
            return self.Flags.INCORRECTEMAILDUPLICATE

    def validatePassword(self):
        if len(self.user.password) > 7:
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTPASSWORD

    def validateUserPassword(self):
        databaseHandler = DatabaseHandler()
        if databaseHandler.ValideUserPasswordByLogin(self.user):
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTUSERPASSWORD

    def validateUserLogin(self):
        if len(self.user.login) > 2:
            return self.Flags.CORRECTFIELD
        else:
            return self.Flags.INCORRECTLOGIN

    def validateLoginExistence(self):
        databaseHandler = DatabaseHandler()
        databaseHandler.createConnection()
        if databaseHandler.findAnyLogin(self.user.login):
            databaseHandler.closeConnection()
            return self.Flags.CORRECTFIELD
        else:
            databaseHandler.closeConnection()
            return self.Flags.INCORRECTELOGINDUPLICATE

    def validateAdvancedUserCode(self, advanced_user_key):
        databaseHandler = DatabaseHandler()
        databaseHandler.createConnection()
        if databaseHandler.findAnyAdvancedUserCode(advanced_user_key):
            return self.Flags.CORRECTFIELD
        return self.Flags.NONEXISTENTADVANCEDUSERKEY

    def validateRegistration(self):
        validationResults = {}
        validationResults["NAME"] = self.validateName()
        validationResults["SURNAME"] = self.validateSurname()
        validationResults["PASSWORD"] = self.validatePassword()
        validationResults["LOGIN"] = self.validateUserLogin()
        validationResults["LOGINEXISTENCE"] = self.validateLoginExistence()
        validationResults["EMAIL"] = self.validateEmail()
        validationResults["EMAILEXISTENCE"] = self.validateEmailExistence()
        return validationResults

    def validateLogin(self):
        validationResults = {}
        validationResults["USERLOGIN"] = self.validateUserLogin()
        if validationResults["USERLOGIN"] == self.Flags.CORRECTFIELD:
            validationResults["USERPASSWORD"] = self.validateUserPassword()
        else:
            validationResults["USERPASSWORD"] = self.Flags.INCORRECTUSERPASSWORD
        return validationResults

    # Correct verification of login
    def validateLoginOperation(self):
        validationResults = {}
        validationResults["LOGINEXISTENCE"] = self.validateLoginExistence()
        if validationResults["LOGINEXISTENCE"] == self.Flags.CORRECTFIELD:
            databaseHandler = DatabaseHandler()
            databaseHandler.createConnection()
            databaseHandler.findUserByLogin(self.user.login)
            hash = databaseHandler.findUserPassword(self.user.id_user)
            if SecurityCreator.verifyPassword(hashed=hash, password=self.user.password):
                validationResults["PASSWORDCORRECTNESS"] = self.Flags.CORRECTFIELD
            else:
                validationResults["PASSWORDCORRECTNESS"] = self.Flags.INCORRECTPASSWORD
        return validationResults
