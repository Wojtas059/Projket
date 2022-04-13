import sqlite3
from typing import List

# isort: split
from src.crypto.security_creator import SecurityCreator
from src.user.user import User
from static.static_config import DATABASE_FILE, MUSCLES_FILE


class DatabaseHandler:

    # Tools for connection administration
    def __init__(self):
        # TODO po przeniesieniu bazy poprawić ścieżkę
        self.databasePath = DATABASE_FILE

    def createConnection(self):
        self.connection = sqlite3.connect(self.databasePath)
        self.cursor = self.connection.cursor()

    def closeConnection(self):
        self.connection.close()

    # Methods for table administration
    def createTableUsers(self):
        try:
            self.cursor.execute(
                """CREATE TABLE Users(id_user integer PRIMARY KEY AUTOINCREMENT,
                                     name varchar(255),surname varchar(255),
                                     login varchar(255) UNIQUE,email varchar(255) UNIQUE,
                                     advanced integer(1))"""
            )
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def dropTableUsers(self):

        try:
            self.cursor.execute("""DROP TABLE Users""")
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def createTablePasswords(self):
        try:
            self.cursor.execute(
                """CREATE TABLE Passwords(id_user integer(11) not null,
                hash varchar(255) not null,advanced_user_key varchar(255))"""
            )
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def dropTablePasswords(self):
        try:
            self.cursor.execute("""DROP TABLE Passwords""")
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def createTableUserAndAdvanced(self):
        try:
            self.cursor.execute(
                """CREATE TABLE UserAndAdvanced(id_user integer(11) not null,
                id_userAdvanced integer(11) not null)"""
            )
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def dropTableUserAndAdvanced(self):
        try:
            self.cursor.execute("""DROP TABLE UserAndAdvanced""")
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def createTableMuscles(self):
        try:
            self.cursor.execute(
                """CREATE TABLE Muscles(id_muscle integer PRIMARY KEY AUTOINCREMENT, name varchar(500))"""
            )
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def dropTableMuscles(self):
        try:
            self.cursor.execute("""DROP TABLE Muscles""")
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(database_error)

    def dropAndCreateTables(self):
        self.createConnection()
        self.dropTablePasswords()
        self.dropTableUsers()
        self.dropTableUserAndAdvanced()
        self.dropTableMuscles()
        self.createTableUsers()
        self.createTablePasswords()
        self.createTableUserAndAdvanced()
        self.createTableMuscles()
        self.fillTablesMuscles()
        self.closeConnection()

    # Creating user section
    # TODO to poprawić zbyteczne zagniżdzenie funkcji w funkcji
    def createUser(self, user: User):

        self.createConnection()
        user = self.insertUser(user)
        self.insertPassword(user)
        self.closeConnection()
        return True

    def insertUser(self, user: User):
        try:
            self.cursor.execute(
                """insert into Users values (null,?,?,?,?,?)""",
                (
                    user.name,
                    user.surname,
                    user.login,
                    user.email,
                    user.advanced,
                ),
            )
            self.connection.commit()
            return self.findUserByLogin(user)
        except sqlite3.Error as database_error:
            print(database_error)
            self.closeConnection()
        return user

    def insertUserAndAdvanced(self, id_user: str, email: str):

        try:
            self.cursor.execute(
                """insert into UserAndAdvanced values (?,?)""",
                (self.findUserIDByEmail(email), id_user),
            )
            self.connection.commit()
            return True
        except sqlite3.Error as database_error:
            print(database_error)
            self.closeConnection()
            return False

    def insertPassword(self, user: User):
        try:
            hashed_password = SecurityCreator.createPassword(user)
            if user.advanced == 0:
                self.cursor.execute(
                    """insert into passwords (id_user,hash) values (?,?)""",
                    (
                        user.id_user,
                        hashed_password,
                    ),
                )
            else:
                advanced_user_key = SecurityCreator.createAdvancedUserCode()
                while not self.findAnyAdvancedUserCode(advanced_user_key):
                    advanced_user_key = SecurityCreator.createAdvancedUserCode()
                self.cursor.execute(
                    """insert into passwords values (?,?,?)""",
                    (
                        user.id_user,
                        hashed_password,
                        advanced_user_key,
                    ),
                )
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(str(database_error) + "Password")
            self.closeConnection()

    # TODO move this method to other class in future
    def generateMusclesNames(self):
        # TODO use config with path
        musclesFile = open(MUSCLES_FILE, "r", encoding="utf-8")
        musclesNames = musclesFile.readlines()
        clearMusclesNames = []

        for name in musclesNames:
            clearMusclesNames.append(name.rstrip())
        for name in clearMusclesNames:
            yield tuple([name])

    # Please use this method in other thread than GUI, for better performance, specially with growing number of muscles
    def fillTablesMuscles(self):
        try:
            self.cursor.executemany(
                """ insert into Muscles (name) values (?) """,
                self.generateMusclesNames(),
            )
            self.connection.commit()
        except sqlite3.Error as database_error:
            print(str(database_error) + " Muscles")
            self.closeConnection()

    def updateTrainerKeyForUser(self, user: User, trainer_key: str):
        try:
            self.cursor.execute(
                """update user set trainer_code=? where id_user=? """,
                (
                    trainer_key,
                    user.id_user,
                ),
            )
        except sqlite3.Error as database_error:
            print(database_error)
            self.closeConnection()

    def updatePassword(self, user: User):
        try:
            hashed_password = SecurityCreator.createPassword(user)

            self.cursor.execute(
                """update passwords set hash= ? where id_user= ? """,
                (
                    hashed_password,
                    user.id_user,
                ),
            )

            self.connection.commit()
        except sqlite3.Error as database_error:
            print(str(database_error) + "Password")
            self.closeConnection()

    # Section of finding functions
    def findUserByLogin(self, user: User):
        self.cursor.execute("select id_user from users where login=?", (user.login,))
        row = self.cursor.fetchone()
        if row is not None:
            user.id_user = row[0]
        else :
            user.id_user = 0
        return user

    def findUserPassword(self, id_user: int):
        print("id " + str(id_user))
        self.cursor.execute("select hash from passwords where id_user=?", (id_user,))
        row = self.cursor.fetchone()
        hash = row[0]
        return hash

    def findAnyAdvancedUserCode(self, advanced_user_key: str):
        self.cursor.execute(
            "select advanced_user_key from passwords where advanced_user_key=?",
            (advanced_user_key,),
        )
        row = self.cursor.fetchone()
        if row is None:
            return True
        return False

    def findAnyLogin(self, login: str):
        self.cursor.execute("select login from users where login=?", (login,))
        row = self.cursor.fetchone()
        if row is None:
            return True
        return False

    def findAnyEmail(self, email: str):
        self.cursor.execute("select login from users where email=?", (email,))
        row = self.cursor.fetchone()
        if row is None:
            return True
        return False

    def findUserIDByEmail(self, email: str):
        id_user = -1
        self.cursor.execute("select id_user from users where email=?", (email,))
        row = self.cursor.fetchone()
        if row is None:
            return id_user
        id_user = row[0]
        return id_user

    def findUsersByTrainerKey(self, trainer_key: str):
        self.cursor.execute(
            """select id_user,name,surname,login from users where trainer_key=? """,
            (trainer_key,),
        )
        users = self.cursor.fetchall()
        return users

    def findUserPrivilegesByLogin(self, login: str):
        self.cursor.execute("""select advanced from users where login=?""", (login,))

        row = self.cursor.fetchone()
        print(row)
        if not row[0]:
            return True
        return False

    def findUserPrivilegesById(self, id_user: int):
        self.cursor.execute(
            """select advanced from users where id_user=?""", (id_user,)
        )

        row = self.cursor.fetchone()
        print(row)
        if not row[0]:
            return True
        return False

    def findUsersForAdvanced(self, id_user: str):
        self.cursor.execute(
            "select id_user from UserAndAdvanced where id_userAdvanced=?", (id_user,)
        )
        listOfUsers = self.cursor.fetchall()
        if listOfUsers is None:
            return False
        return listOfUsers

    def findUserByIdList(self, ids: List):
        query = "select * from users where id_user in ({seq})".format(
            seq=",".join(["?"] * len(ids))
        )
        self.cursor.execute(query, ids)
        usersList = self.cursor.fetchall()
        return usersList

    def findUserById(self, ids: str):
        query = f"select * from users where id_user in ({','.join(['?']*len(ids))})"
        self.cursor.execute(query, ids)
        usersList = self.cursor.fetchall()
        return usersList

    def findUsersNamesforAdvance(self, listOfUser: List):
        usersList = []
        for user in listOfUser:
            usersList.append(self.findUserById(user[0]))
        usersList = self.findUserByIdList(usersList)
        for user in listOfUser:
            print(user)

    def getUserCredentials(self, login: str):
        self.cursor.execute(
            "select id_user,name,surname,email from users where login=?", (login,)
        )
        row = self.cursor.fetchone()
        return row

    def getAllMuscles(self):
        query = "select * from Muscles"
        self.cursor.execute(query)
        musclesList = self.cursor.fetchall()
        return musclesList

    # Validators
    def ValideUserPasswordByLogin(self, user: User):
        self.createConnection()
        hashed = self.findUserPassword(self.findUserByLogin(user).id_user)
        self.closeConnection()
        return SecurityCreator.verifyPassword(hashed, user.password)
