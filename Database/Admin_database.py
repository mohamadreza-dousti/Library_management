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
                gender TEXT,
                age INTEGER,
                code_meli TEXT,
                user_name TEXT,
                password TEXT
            )
        ''')
        self.con.commit()

    def register_admin(self, name, fname, gender, age, code_meli, user_name, password):
        self.cursor.execute('''
        INSERT INTO admins (name, f_name, gender, age, code_meli, user_name, password)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, fname, gender, age, code_meli, user_name, password))
        self.con.commit()

    
    def remove_admin(self, code_meli):
        self.cursor.execute('DELETE FROM admins WHERE code_meli = ?', (code_meli,))
        self.con.commit()
    
    def get_pass_admin(self, user_name):
        self.cursor.execute('SELECT password FROM admins WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()

    def close(self):
        self.con.close()