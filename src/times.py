from datetime import datetime
import sqlite3


class Times:
    def __init__(self, db_path="times.sqlite"):
        self.conn = sqlite3.connect(db_path)
        self.cur = self.conn.cursor()
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
        now = str(datetime.now())
        self.conn.execute(sql, (now, message))
        self.conn.commit()

    def recall(self, n=10):
        sql = """SELECT * FROM times"""
        self.cur.execute(sql)
        for i in self.cur.fetchall():
            print(i)

    def __del__(self):
        self.cur.close()
        self.conn.commit()
        self.conn.close()
