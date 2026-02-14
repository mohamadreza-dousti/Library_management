from Database.Book_database import BookDB
import customtkinter as ctk
import re

class Book:
    total_books = 0
    def __init__(self, name, author=None, status=None):
        self.name = name
        self.author = author
        self.status = status
    
    @classmethod
    def AddTotalBooks(cls):
        cls.total_books += 1
    
    @classmethod
    def RemoveTotalBooks(cls):
        cls.total_books -= 1

    @classmethod
    def getTotalBooks(cls):
        return cls.total_books

    
class BookMnagement():
    def __init__(self):
        self.db = BookDB()
        self.db.create_table()
        self.db.close

    def AddBook(self, name, author, status, btn):
        self.name = name.get()
        self.author = author.get()
        self.status = status.get()
        book = Book(self.name, self.author, self.status)
        add = BookDB()
        add.add_book(self.name, self.author, self.status)
        add.close()
        book.AddTotalBooks()
        btn.configure(state='disabled')


    def RemoveBook(self, name, btn):
        self.name = name.get()
        remove = BookDB()
        remove.remove_book(self.name)
        remove.close()
        book = Book(self.name)
        book.RemoveTotalBooks()
        btn.configure(state='disabled')
        
    
    def ShowBooks(self):
        books = BookDB()
        result = books.show_books()
        books.close()
        return result


    def SearchBook(self, name, val, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        result= []
        self.name = name.get()
        self.val = val.get()
        books = BookDB()
        if self.val == '1':
            ansewr = books.show_books1()
        elif self.val == '0':
            ansewr = books.show_books0()
        else:
            ansewr = books.show_books()
        books.close()

        for book in ansewr:
            if re.match(f'.*{self.name}.*', book[0]):
                result.append(book)

        scroll_frame = ctk.CTkScrollableFrame(frame, height=10)
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