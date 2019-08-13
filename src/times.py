from datetime import datetime
import sqlite3

# import dataclass


class Times:
    def __init__(self, db_path="times.sqlite"):
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS times
             (id INTEGER PRIMARY KEY AUTOINCREMENT,
              message TEXT,
              time TEXT)"""
        self.conn.execute(sql)
        self.conn.commit()

    def post(self, message: str):
        sql = """INSERT INTO times (time,message) values(?,?)"""
        self.conn.execute(sql, ("time", message))
        self.conn.commit()

    def recall(self, n):
        sql = """SELECT time,message FROM times"""
        r = self.conn.execute(sql)
        print(r)
