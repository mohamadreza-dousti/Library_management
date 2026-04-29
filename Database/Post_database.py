import sqlite3

class PostDB:
    def __init__(self):
        self._db_name = 'Database\Library_database.db'
        self.con = sqlite3.connect(self._db_name)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                name TEXT,
                f_name TEXT,
                gender TEXT,
                age INTEGER,
                code_meli TEXT,
                user_name TEXT,
                password TEXT,
                id INTEGER PRIMARY KEY
            )
        ''')
        self.con.commit()

    def register_post(self, name, fname, age, code_meli, user_name, password, gender, id):
        self.cursor.execute('''
        INSERT INTO posts (name, f_name, gender, age, code_meli, user_name, password, id)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, fname, gender, age, code_meli, user_name, password, id))
        self.con.commit()

    
    def remove_post(self, user_name):
        self.cursor.execute('DELETE FROM posts WHERE code_meli = ?', (user_name,))
        self.con.commit()
    
    def get_pass_post(self, user_name):
        self.cursor.execute('SELECT password FROM posts WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()

    def get_id_person(self, username):
        self.cursor.execute('SELECT id From posts WHERE user_name = ?', (username,))
        return self.cursor.fetchone()

    def get_id(self):
        self.cursor.execute('SELECT id FROM posts')
        return self.cursor.fetchall()

    def close(self):
        self.con.close()