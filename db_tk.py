import sqlite3

class Database:
    def __init__(self, db):
        self.con = sqlite3.connect(db)
        self.cur = self.con.cursor()
        self.cur.execute('''CREATE TABLE IF NOT EXISTS person
                             (id INTEGER PRIMARY KEY, lname TEXT, fname TEXT, password TEXT, name_w TEXT)''')
        self.con.commit()

    def insert(self, fname, lname, password, name_w):
        self.cur.execute('INSERT INTO person VALUES (NULL, ?, ?, ?, ?)', (lname, fname, password, name_w))
        self.con.commit()

    def fetch(self):
        self.cur.execute('SELECT * FROM person')
        result = self.cur.fetchall()
        return result

    def remove(self, id):
        self.cur.execute('DELETE FROM person WHERE id = ?', (id,))
        self.con.commit()

    def update(self, id, lname, fname, password, name_w):
        self.cur.execute('''UPDATE person 
                             SET lname = ?, fname = ?, password = ?, name_w = ? 
                             WHERE id = ?''', (lname, fname, password, name_w, id))
        self.con.commit()

    def search(self, i):
        self.cur.execute('''SELECT * FROM person 
                             WHERE lname = ? OR fname = ? OR password = ? OR name_w = ?''', (i, i, i, i))
        return self.cur.fetchall()
