import random

import bcrypt

from src.user.user import User


class SecurityCreator:
    def createAdvancedUserCode():
        ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        chars = []
        for i in range(16):
            chars.append(random.choice(ALPHABET))
        return "".join(chars)

    def createPassword(user: User):
        password = str.encode(user.password)
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed_password.decode()

    def verifyPassword(hashed: str, password: str):
        password = password.encode()
        hashed = hashed.encode()
        if bcrypt.checkpw(password, hashed):
            return True
        else:
            return False

    def createPasswordByUserPassword(password: str):
        password = str.encode(password)
        hashed_password = bcrypt.hashpw(password, bcrypt.gensalt())
        return hashed_password.decode()
