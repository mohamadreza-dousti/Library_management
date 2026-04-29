from Database.Book_database import BookDB, PostBookDB, TrustDB, OnlineBookDB
from Database.User_database import UserDB
import customtkinter as ctk
import re
import datetime

class Book:
    def __init__(self, name, author, id):
        self.name = name
        self.author = author
        self.id = id

    def create_book(self):
        add = BookDB()
        add.add_book(self.name, self.author, self.id)
        add.close()
    
class BookMnagement():
    def __init__(self):
        self.db = BookDB()
        self.db.create_table()
        self.db.close

    def AddBook(self, name, author, id, btn):
        self.name = name.get()
        self.author = author.get()
        self.id = id.get()
        book = Book(self.name, self.author, self.id)
        book.create_book()
        btn.configure(state='disabled')


    def RemoveBook(self, id, btn):
        self.id = id.get()
        remove = BookDB()
        remove.remove_book(self.id)
        remove.close()
        btn.configure(state='disabled')
        
    
    def ShowBooks(self, val, frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        ansewr = []

        scroll_frame = ctk.CTkScrollableFrame(frame, width=250, height=30)
        scroll_frame.pack(pady=15)
        scroll_frame.grid_columnconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(1, weight=1)
        scroll_frame.grid_columnconfigure(2, weight=1)

        self.val = val.get()
        books = BookDB()
        if self.val == '1':
            ansewr = books.show_books1()
        elif self.val == '0':
            ansewr = books.show_books0()
        else:
            ansewr = books.show_books()
        books.close()

        i=0
        for book in ansewr:
            book_title = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'title:{book[0]}')
            book_title.grid(row=i, column=0, pady=5)
            book_author = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'author:{book[1]}')
            book_author.grid(row=i, column=1)
            book_status = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'status:{book[2]}')
            book_status.grid(row=i, column=2)
            i += 1


    def SearchBook(self, name, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        result= []
        self.name = name.get()
        books = BookDB()
        ansewr = books.show_books()
        books.close()

        for book in ansewr:
            if re.match(f'.*{self.name}.*', book[0]):
                result.append(book)

        scroll_frame = ctk.CTkScrollableFrame(frame, width=280)
        scroll_frame.pack(pady=5)
        scroll_frame.grid_columnconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(1, weight=1)
        scroll_frame.grid_columnconfigure(2, weight=1)
        
        i=0
        for book in result:
            book_title = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'title:{book[0]}')
            book_title.grid(row=i, column=0)
            book_author = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'author:{book[1]}')
            book_author.grid(row=i, column=1)
            book_status = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'status:{book[2]}')
            book_status.grid(row=i, column=2)
            i += 1
    
    def Posted(self, book_id, btn, title, pid, code):
        posted = OnlineBookDB()
        date = datetime.datetime.now()
        year = date.year
        month = date.month
        day = date.day
        self.pid = pid.get()
        self.title = title.cget('text')
        self.bid = book_id.cget('text')
        posted.update_posted(self.bid)
        posted.close()
        post_book = PostBookDB()
        post_book.create_table()
        post_book.add_book(self.title, self.bid, self.pid, year, month, day, code)
        post_book.close()
        btn.configure(state='disabled', text='posted')
    
    def update_status(self, id, btn):
        self.id = id.get()
        update = BookDB()
        update.update_status(self.id)
        update.close()
        delete = TrustDB()
        delete.remove_book(self.id)
        delete.close()
        btn.configure(state='disabled')
    
    def lend_book(self, code, id, btn):
        get_info = UserDB()
        date = datetime.datetime.now()
        month = date.month+1
        day = date.day
        self.code = code.get()
        self.id = id.get()
        self.user_name = f'u-{self.code}'
        self.name = get_info.get_name(self.user_name)[0]
        self.fname = get_info.get_fname(self.user_name)[0]
        self.phone = get_info.get_phone(self.user_name)[0]
        get_info.close()
        lend = TrustDB()
        lend.create_table()
        lend.add_book(self.name, self.fname, self.phone, month, day, self.id, self.user_name)
        lend.close()
        update = BookDB()
        update.update_status_0(self.id)
        btn.configure(state='disabled')