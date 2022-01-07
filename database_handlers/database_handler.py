import sqlite3
from User.user import User
from crypto.securityCreator import SecurityCreator


class DatabaseHandler():

    # Tools for connection administration
    def __init__(self):
        self.databasePath = '.\database\database.db'

    def createConnection(self):
        self.connection = sqlite3.connect(self.databasePath)
        self.cursor = self.connection.cursor()

    def closeConnection(self):
        self.connection.close()

    # Methods for table administration
    def createTableUsers(self):
        try:
            self.cursor.execute(
                '''CREATE TABLE Users(id_user integer PRIMARY KEY AUTOINCREMENT, name varchar(255),
                surname varchar(255),login varchar(255) UNIQUE,email varchar(255) UNIQUE,trainer_key varchar(255),advanced integer(1))''')
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def dropTableUsers(self):

        try:
            self.cursor.execute(
                '''DROP TABLE Users''')
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def createTablePasswords(self):
        try:
            self.cursor.execute(
                '''CREATE TABLE Passwords(id_user integer(11) not null,
                hash varchar(255) not null,advanced_user_key varchar(255))''')
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def dropTablePassword(self):
        try:
            self.cursor.execute(
                '''DROP TABLE Passwords''')
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def dropAndCreateTables(self):
        self.createConnection()
        self.dropTablePassword()
        self.dropTableUsers()
        self.createTableUsers()
        self.createTablePasswords()
        self.closeConnection()

    # Creating user section
    def createUser(self, user: User):

        self.createConnection()
        user = self.insertUser(user)
        self.insertPassword(user)
        self.closeConnection()
        return True

    def insertUser(self, user: User):
        try:
            self.cursor.execute(
                '''insert into Users values (null,?,?,?,?,null,?)''', (user.name, user.surname, user.login, user.email, user.advanced,))
            self.connection.commit()
            return self.findUserByLogin(user)
        except sqlite3.Error as database_error:
            print(database_error)
            self.closeConnection()
        return user

    def insertPassword(self, user: User):
        try:
            hashed_password = SecurityCreator.createPassword(user)
            if(user.advanced == 0):
                self.cursor.execute(
                    '''insert into passwords (id_user,hash) values (?,?)''', (user.id_user, hashed_password,))
            else:
                advanced_user_key = SecurityCreator.createAdvancedUserCode()
                while(not self.findAnyAdvancedUserCode(advanced_user_key)):
                    advanced_user_key = SecurityCreator.createAdvancedUserCode()
                self.cursor.execute('''insert into passwords values (?,?,?)''',
                                    (user.id_user, hashed_password, advanced_user_key,))
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(str(database_error)+"Password")
            self.closeConnection()

    def updateTrainerKeyForUser(self, user: User, trainer_key: str):
        try:
            self.cursor.execute(
                '''update user set trainer_code=? where id_user=? ''', (trainer_key, user.id_user,))
        except sqlite3.Error as database_error:
            print(database_error)
            self.closeConnection()

    # Section of finding functions
    def findUserByLogin(self, user: User):
        self.cursor.execute(
            "select id_user from users where login=?", (user.login,))
        row = self.cursor.fetchone()
        user.id_user = row[0]
        return user

    def findUserPassword(self, id_user: int):
        self.cursor.execute(
            "select hash from passwords where id_user=?", (id_user,))
        row = self.cursor.fetchone()
        hash = row[0]
        return hash

    def findAnyAdvancedUserCode(self, advanced_user_key: str):
        self.cursor.execute(
            "select advanced_user_key from passwords where advanced_user_key=?", (advanced_user_key,))
        row = self.cursor.fetchone()
        if(row == None):
            return True
        return False

    def findAnyLogin(self, login: str):
        self.cursor.execute(
            "select login from users where login=?", (login,))
        row = self.cursor.fetchone()
        if(row == None):
            return True
        return False

    def findAnyEmail(self, email: str):
        self.cursor.execute(
            "select login from users where email=?", (email,))
        row = self.cursor.fetchone()
        if(row == None):
            return True
        return False

    def findUsersByTrainerKey(self, trainer_key: str):
        self.cursor.execute(
            '''select id_user,name,surname,login from users where trainer_key=? ''', (
                trainer_key,)
        )
        users = self.cursor.fetchall()
        return users

    def findUserPrivilegesByLogin(self, login: str):
        self.cursor.execute(
            '''select advanced from users where login=?''', (login,)
        )
        row = self.cursor.fetchone()
        if row[0]:
            return True
        return False

    # Validators
    def ValideUserPasswordByLogin(self, user: User):
        self.createConnection()
        hashed = self.findUserPassword(self.findUserByLogin(user))
        self.closeConnection()
        return SecurityCreator.verifyPassword(hashed, user.password)
