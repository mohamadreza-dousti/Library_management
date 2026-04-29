from Database.Book_database import BookDB
import customtkinter as ctk
from Database.Book_database import BookDB, OnlineBookDB
from USER.Profile_management.profile import ProfileManagement as pmng
import datetime
import re

class reserveBook():
    def __init__(self, username):
        self.username = username

    def search_book_user(self, title, frame):
        for widget in frame.winfo_children():
            widget.destroy()
            
        result= []
        self.name = title.get()
        books = BookDB()
        ansewr = books.show_books()
        books.close()
        for book in ansewr:
            if re.match(f'.*{self.name}.*', book[0]):
                result.append(book)
        
        i=0
        title_vars = {}
        author_vars = {}
        status_vars = {}
        reserve_vars = {}
        for book in result:
            title_vars[f'book_title{i}'] = ctk.CTkLabel(frame, fg_color='black', text=f'{book[0]}', width=110)
            title_vars[f'book_title{i}'].grid(row=i, column=0)
            author_vars[f'book_author{i}'] = ctk.CTkLabel(frame, fg_color='black', text=f'{book[1]}', width=100)
            author_vars[f'book_author{i}'].grid(row=i, column=1)
            status_vars[f'book_status{i}'] = ctk.CTkLabel(frame, fg_color='black', text=f'{book[2]}', width=10)
            status_vars[f'book_status{i}'].grid(row=i, column=2)
            if book[2]:
                reserve_vars[f'reserve{i}'] = ctk.CTkButton(frame, text='reserve', corner_radius=10, width=75, command=lambda ctr=i : self.reserve(title_vars[f'book_title{ctr}'], reserve_vars[f'reserve{ctr}']))
                reserve_vars[f'reserve{i}'].grid(row=i, column=3)
            else:
                reserve_vars[f'reserve{i}'] = ctk.CTkButton(frame, text='reserved', corner_radius=10, fg_color='red', state='disabled', width=75)
                reserve_vars[f'reserve{i}'].grid(row=i, column=3)
            i += 1
    
    def reserve(self, name, btn):
        self.title = name.cget('text')
        manage = pmng(self.username)
        membership_date = datetime.datetime.now()
        year = membership_date.year
        month = membership_date.month
        day = membership_date.day
        code = manage.get_id()[0]
        online = OnlineBookDB()
        online.create_table()
        res = BookDB()
        res.reserve_book(self.title)
        id = res.get_id(self.title)[0]
        online.add_book(id, code, year, month, day)
        res.close()
        online.close()
        btn.configure(state='disabled', text='reserved', fg_color='red')