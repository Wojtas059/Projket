from queue import Queue
from threading import Thread

from src.database_handlers.database_handler import DatabaseHandler


class DatabaseInserter(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.runner = True
        self.database_handler = DatabaseHandler()
        self.table_name = ""
        self.mode = 0

    def run(self):
        self.database_handler.createConnection()
        self.table_name = self.database_handler.createResultTable()
        while self.runner:
            if self.database_handler.DataQueue.qsize() > 99:
                self.database_handler.insertDataToDB(self.table_name)

    def stop(self):
        self.runner = False
        self.database_handler.insertDataToDB(self.table_name, self.mode)
        self.database_handler.closeConnection()
