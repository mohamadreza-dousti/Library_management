import sqlite3

class UserDB:
    def __init__(self):
        self._db_name = 'Database\\Library_database.db'
        self.con = sqlite3.connect(self._db_name)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                name TEXT,
                f_name TEXT,
                age INTEGER,
                gender TEXT,
                code_meli TEXT,
                address TEXT,
                user_name TEXT,
                password TEXT,
                year INTEGER,
                month INTEGER,
                day INTEGER, 
                expire_year INTEGER,
                book_count INTEGER,
                chair BOOLIAN DEFAULT 0,
                phone TEXT
            )
        ''')
        self.con.commit()

    def add_user(self, name, fname, age, gender, code_meli, address, user_name, password, year, month, day, expire_year, book_count, phone):
        self.cursor.execute('''
        INSERT INTO users (name, f_name, age, gender, code_meli, address, user_name, password, year, month, day, expire_year, book_count, phone)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (name, fname, age, gender, code_meli, address, user_name, password, year, month, day, expire_year, book_count, phone))
        self.con.commit()

    
    def remove_user(self, code_meli):
        self.cursor.execute('DELETE FROM users WHERE code_meli = ?', (code_meli,))
        self.con.commit()
    
    def show_users(self):
        self.cursor.execute('SELECT * FROM users')
        return self.cursor.fetchall()

    def get_pass_user(self, user_name):
        self.cursor.execute('SELECT password FROM users WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()

    def get_name(self, user_name):
        self.cursor.execute('SELECT name FROM users WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()

    def get_fname(self, user_name):
        self.cursor.execute('SELECT f_name FROM users WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()

    def get_age(self, user_name):
        self.cursor.execute('SELECT age FROM users WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()

    def get_phone(self, user_name):
        self.cursor.execute('SELECT phone FROM users WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()
    
    def get_gender(self, user_name):
        self.cursor.execute('SELECT gender FROM users WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()

    def get_id(self, user_name):
        self.cursor.execute('SELECT code_meli FROM users WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()
    
    def get_address(self, user_name):
        self.cursor.execute('SELECT address FROM users WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()
    
    def get_membership_date(self, user_name):
        self.cursor.execute('SELECT year, month, day FROM users WHERE user_name = ?', (user_name,))
        year, month, day = self.cursor.fetchone()
        return year, month, day
    
    def get_expire_date(self, user_name):
        self.cursor.execute('SELECT expire_year, month, day FROM users WHERE user_name = ?', (user_name,))
        year, month, day = self.cursor.fetchone()
        return year, month, day
    
    def close(self):
        self.con.close()