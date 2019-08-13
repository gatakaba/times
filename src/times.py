from datetime import datetime
import sqlite3

# import dataclass


class Times:
    def __init__(self, db_path="times.sqlite"):
        self.conn = sqlite3.connect(db_path)

    def _create_table(self):
        sql = """CREATE TABLE IF NOT EXISTS times
             (id INTEGER PRIMARY KEY,
              message TEXT,
              time TEXT)"""
        self.conn.execute(sql)
        self.conn.commit()

    def post(self, content):
        message = Message(content)

    def recall(self, n):
        pass


# @dataclasses.dataclass
class Message:
    def __init__(self, message: str, dt: datetime):
        self.dt = dt
        self.message = message
