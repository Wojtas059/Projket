import random
import bcrypt

from User.user import User



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

    def verifyPassword(hashed:str,password:str):
        password = str.encode(password)
        if bcrypt.checkpw(password, hashed):
            return True
        else:
            return False
