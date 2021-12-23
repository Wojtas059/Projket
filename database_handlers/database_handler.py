import sqlite3
from User.user import User
from crypto.securityCreator import SecurityCreator








class DatabaseHandler():

    def __init__(self):
        self.databasePath='repo\database\database.db'

    def createConnection(self):
        self.connection = sqlite3.connect(self.databasePath)
        self.cursor = self.connection.cursor()

    def closeConnection(self):
        self.connection.close()

    def createTableUsers(self):
        try:
            self.cursor.execute(
                '''CREATE TABLE Users(id_user integer PRIMARY KEY AUTOINCREMENT, name varchar(255),
                surname varchar(255),login varchar(255) UNIQUE,email varchar(255) UNIQUE,advanced integer(1))''')
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
                '''DROP TABLE Password''')
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def createUser(self, user:User):
        self.createConnection()
        self.insertPassword(self.insertUser(user))
        self.closeConnection()

    def insertUser(self, user:User):
        try:
            self.cursor.execute(
                '''insert into Users values ({name},{surname},{login},{email},{advanced}})'''.format(name=user.name, surname=user.surname, login=user.login, email=user.email, advanced=user.advanced))
            self.connection.commit()
            return self.findUserByLogin(user)
        except sqlite3.Error as database_error:
            print(database_error)
            return user

    def insertPassword(self, user:User):
        hashed_password = SecurityCreator.createPassword(user)
        if(user.advanced):
            self.cursor.execute('''insert into passwords (id_user,hash) values ({id_user},{hash})'''.format(
                id_user=user.id_user, hash=hashed_password))
        else:
            advanced_user_key=SecurityCreator.createAdvancedUserCode()
            while(self.findAnyAdvancedUserCode(advanced_user_key)):
                    advanced_user_key=SecurityCreator.createAdvancedUserCode()
            self.cursor.execute('''insert into passwords values ({id_user},{hash},{advanced_user_key})'''.format(
                id_user=user.id_user, hash=hashed_password, advanced_user_key=advanced_user_key))
        self.connection.commit()

    def findUserByLogin(self,user:User):
        self.cursor.execute(
                "select id_user from users where login={login}".format(login=user.login))
        row = self.cursor.fetchone()
        user.id_user = row['id_user']
        return user

    def findUserPassword(self,id_user:int):
        self.cursor.execute(
                "select hash from passwords where id_user={id_user}".format(id_user=id_user))
        row = self.cursor.fetchone()
        hash = row['hash']
        return hash
    def findAnyAdvancedUserCode(self,advanced_user_key:str):
        self.cursor.execute(
                "select advanced_user_key from passwords where advanced_user_key={advanced_user_key}".format(advanced_user_key=advanced_user_key))
        row = self.cursor.fetchone()
        if(row==None):
            return True
        return False
    def findAnyLogin(self,login:str):
        self.cursor.execute(
                "select login from users where login={login}".format(login=login))
        row = self.cursor.fetchone()
        if(row==None):
            return True
        return False
    def findAnyEmail(self,email:str):
        self.cursor.execute(
                "select login from users where email={email}".format(email=email))
        row = self.cursor.fetchone()
        if(row==None):
            return True
        return False

    def ValideUserPasswordByLogin(self,user:User):
        self.createConnection()
        hashed=self.findUserPassword(self.findUserByLogin(user))
        self.closeConnection()
        return SecurityCreator.verifyPassword(hashed,user.password)


