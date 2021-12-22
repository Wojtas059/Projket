import random
import bcrypt

from User.user import User
from database.database_handler import DatabaseHandler


class SecurityCreator():

    def createAdvancedUserCode(self):
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars = []
        for i in range(16):
            chars.append(random.choice(ALPHABET))
        return "".join(chars)

    def createPassword(user: User):
        password = str.encode(user.password)
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed_password

    def verifyPassword(user: User):
        databaseHandler=DatabaseHandler
        databaseHandler.createConnection()
        hashed=databaseHandler.findUserPassword(databaseHandler.findUserByLogin(user))
        databaseHandler.closeConnection()
        password = str.encode(user.password)
        if bcrypt.checkpw(password, hashed):
            return True
        else:
            return False
