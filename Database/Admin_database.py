import sqlite3

class AdminDB:
    def __init__(self):
        self._db_name = 'Database\Library_database.db'
        self.con = sqlite3.connect(self._db_name)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS admins (
                name TEXT,
                f_name TEXT,
                age INTEGER,
                user_name TEXT,
                password TEXT,
                gender TEXT,
                year INTEGER,
                month INTEGER,
                day INTEGER
            )
        ''')
        self.con.commit()

    def register_admin(self, name, fname, age, user_name, password, gender, year, mont, day):
        self.cursor.execute('''
        INSERT INTO admins (name, f_name, age, user_name, password, gender, year, month, day)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, fname, age, user_name, password, gender, year, mont, day))
        self.con.commit()

    
    def remove_admin(self, user_name):
        self.cursor.execute('DELETE FROM admins WHERE user_name = ?', (user_name,))
        self.con.commit()
    
    def get_pass_admin(self, user_name):
        self.cursor.execute('SELECT password FROM admins WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()

    def close(self):
        self.con.close()