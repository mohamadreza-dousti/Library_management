import sqlite3

class BookDB:
    def __init__(self):
        self._db_name = 'Database\Library_database.db'
        self.con = sqlite3.connect(self._db_name)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS books (
            title TEXT,
            author TEXT,
            status BOOLEAN DEFAULT 1,
            id INTEGER PRIMATY KEY,
            online_reserve BOOLEAN DEFAULT 0
            )
        ''')
        self.con.commit()

    def add_book(self, title, author, id):
        self.cursor.execute('''
        INSERT INTO books (title, author, id)
        VALUES (?, ?, ?)
        ''', (title, author, id))
        self.con.commit()

    
    def remove_book(self, id):
        self.cursor.execute('DELETE FROM books WHERE id = ?', (id,))
        self.con.commit()
    
    def show_books(self):
        self.cursor.execute('SELECT * FROM books')
        return self.cursor.fetchall()
    
    def show_books1(self):
        self.cursor.execute('SELECT * FROM books WHERE status = ?', ('1',))
        return self.cursor.fetchall()
    
    def show_books0(self):
        self.cursor.execute('SELECT * FROM books WHERE status = ?', ('0',))
        return self.cursor.fetchall()
    
    def reserve_book(self, name):
        self.cursor.execute('UPDATE books SET status = ? WHERE title = ?', (0, name))
        self.con.commit()
    
    def update_status(self, id):
        self.cursor.execute('UPDATE books SET status = ? WHERE id = ?', (1, id))
        self.con.commit()
    
    def update_status_0(self, id):
        self.cursor.execute('UPDATE books SET status = ? WHERE id = ?', (0, id))
        self.con.commit()
    
    def get_id(self, title):
        self.cursor.execute('SELECT id FROM books WHERE title = ?', (title,))
        return self.cursor.fetchone()

    def get_title(self, id):
        self.cursor.execute('SELECT title FROM books WHERE id = ?', (id,))
        return self.cursor.fetchone()
    
    def close(self):
        self.con.close()

class PostBookDB:
    def __init__(self):
        self._db_name = 'Database\Library_database.db'
        self.con = sqlite3.connect(self._db_name)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS post_books (
                post_id INTEGER,
                name TEXT,
                book_id INTEGER,
                year INTEGER,
                month INTEGER,
                day INTEGER,
                arrived BOOLEAN DEFAULT 0,
                code_meli TEXT,
                FOREIGN KEY (book_id) REFERENCES books(id)
            )
        ''')
        self.con.commit()

    def add_book(self, title, b_id, p_id, year, month, day, code_meli):
        self.cursor.execute('''
        INSERT INTO post_books (post_id, name, book_id, year, month, day, code_meli)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (p_id, title, b_id, year, month, day, code_meli))
        self.con.commit()

    def remove_book(self, bid):
        self.cursor.execute('DELETE FROM post_books WHERE book_id = ?', (bid,))
        self.con.commit()
    
    def show_books(self, id):
        self.cursor.execute(f'SELECT * FROM post_books WHERE post_id = {id} AND arrived = {0}')
        return self.cursor.fetchall()

    
    def update_arrive(self, book_id):
        self.cursor.execute('UPDATE post_books SET arrived = ? WHERE book_id = ?', (1, book_id))
        self.con.commit()

    def close(self):
        self.con.close()

class TrustDB:
    def __init__(self):
        self._db_name = 'Database\Library_database.db'
        self.con = sqlite3.connect(self._db_name)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS trusts (
                name TEXT,
                f_name TEXT,
                phone TEXT,
                valid_month INTEGER,
                vlid_day INTEGER,
                id INTEGER,
                user_name TEXT,
                FOREIGN KEY (id) REFERENCES books(id)
            )
        ''')
        self.con.commit()

    def add_book(self, name, fname, phone, month, day, id, username):
        self.cursor.execute('''
        INSERT INTO trusts (name, f_name, phone, valid_month, vlid_day, id, user_name)
        VALUES (?, ?, ?, ?, ?, ?, ?)
        ''', (name, fname, phone, month, day, id, username))
        self.con.commit()

    
    def remove_book(self, id):
        self.cursor.execute('DELETE FROM trusts WHERE id = ?', (id,))
        self.con.commit()

    def close(self):
        self.con.close()

class OnlineBookDB:
    def __init__(self):
        self._db_name = 'Database\Library_database.db'
        self.con = sqlite3.connect(self._db_name)
        self.cursor = self.con.cursor()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS online_books (
                            id INTEGER,
                            year INTEGER,
                            month INTEGER,
                            day INTEGER,
                            code_meli TEXT,
                            posted BOOLEAN DEFAULT 0,
                            FOREIGN KEY (id) REFERENCES books(id)                            
            )
        ''')
        self.con.commit()

    def add_book(self, id, code_meli, year, month, day):
        self.cursor.execute('''
        INSERT INTO online_books (id, year, month, day, code_meli)
        VALUES (?, ?, ?, ?, ?)
        ''', (id, year, month, day, code_meli))
        self.con.commit()
    
    def update_posted(self, id):
        self.cursor.execute('UPDATE online_books SET posted = ? WHERE id = ?', (1, id))
        self.con.commit()

    def show_books(self):
        self.cursor.execute('SELECT * FROM online_books WHERE posted = ?', (0,))
        return self.cursor.fetchall()

    def close(self):
        self.con.close()

    