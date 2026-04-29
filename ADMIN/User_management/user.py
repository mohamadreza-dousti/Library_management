import datetime
from Database.User_database import UserDB
import customtkinter as ctk

class User:
    def __init__(self, name, fname, age, gender, code_meli, address, phone):
        self.name = name
        self.fname = fname
        self.age = age
        self.user_code = f'u-{code_meli}'
        self.password = f'u{code_meli}'
        self.code = code_meli
        self.gender = gender
        self.membership_date = datetime.datetime.now()
        self.year = self.membership_date.year
        self.month = self.membership_date.month
        self.day = self.membership_date.day
        self.expire_year = self.year + 1
        self.book_count = 0
        self.phone = phone
        self.address = address
    
    def create_user(self):
        add = UserDB()
        add.add_user(self.name, self.fname, self.age, self.gender, self.code, self.address, self.user_code, self.password, self.year, self.month, self.day, self.expire_year, self.book_count, self.phone)
        add.close()

class UserManagement:
    def __init__(self):
        self.db = UserDB()
        self.db.create_table()
        self.db.close()
    
    def AddUser(self, name, fname, age, gender, code_meli, address, phone, btn):
        self.name = name.get()
        self.fname = fname.get()
        self.age = age.get()
        self.code_meli = code_meli.get()
        self.gender = gender.get()
        self.phone = phone.get()
        self.address = address.get()
        user = User(self.name, self.fname, self.age, self.gender, self.code_meli, self.address, self.phone)
        user.create_user()
        btn.configure(state='disabled')


    def RemoveUser(self, code_meli, btn):
        self.code_meli = code_meli.get()
        remove = UserDB()
        remove.remove_user(self.code_meli)
        remove.close()
        btn.configure(state='disabled')
        
    
    def ShowUsers(self):
        users = UserDB()
        result = users.show_users()
        users.close()
        return result


    def SearchUser(self, code_meli, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        self.code_meli = code_meli.get()
        users = UserDB()
        result = users.show_users()
        users.close()

        for user in result:
            if user[4] == self.code_meli:
                ansewr = user
                fullname = ctk.CTkLabel(frame, text=f'fullname : {ansewr[0]} {ansewr[1]}')
                fullname.pack(pady=1)
                age = ctk.CTkLabel(frame, text=f'age : {ansewr[2]}')
                age.pack(pady=2)
                gender = ctk.CTkLabel(frame, text=f'gender : {ansewr[3]}')
                gender.pack(pady=2)
                code_meli = ctk.CTkLabel(frame, text=f'code meli : {ansewr[4]}')
                code_meli.pack(pady=2)
                trust_date = ctk.CTkLabel(frame, text=f'trust date : {ansewr[11]}\{ansewr[9]}\{ansewr[10]}')
                trust_date.pack(pady=2)
                break
