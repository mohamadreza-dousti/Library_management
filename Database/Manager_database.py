import sqlite3

class ManagerDB:
    def __init__(self):
        self._db_name = 'Database\Library_database.db'
        self.con = sqlite3.connect(self._db_name)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS manager (
                user_name TEXT,
                password TEXT
            )
        ''')
        self.con.commit()
    
    def get_pass_manager(self, user_name):
        self.cursor.execute('SELECT password FROM manager WHERE user_name = ?', (user_name,))
        return self.cursor.fetchone()

    def close(self):
        self.con.close()
