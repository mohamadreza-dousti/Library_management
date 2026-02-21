import datetime
from Database.User_database import UserDB
import customtkinter as ctk

class User:
    def __init__(self, name, fname, age, code_meli, gender):
        self.name = name
        self.fname = fname
        self.age = age
        self.user_code = f'u-{code_meli}'
        self.password = f'u{code_meli}'
        self.gender = gender
        self.membership_date = datetime.datetime.now()
        self.year = self.membership_date.year
        self.month = self.membership_date.month
        self.day = self.membership_date.day
        self.expire_year = self.year + 1
    
    def create_user(self):
        add = UserDB()
        add.add_user(self.name, self.fname, self.age, self.user_code, self.password, self.gender, self.year, self.month, self.day, self.expire_year)
        add.close()

class UserManagement:
    def __init__(self):
        self.db = UserDB()
        self.db.create_table()
        self.db.close()
    
    def AddUser(self, name, fname, age, code_meli, gender, btn):
        self.name = name.get()
        self.fname = fname.get()
        self.age = age.get()
        self.code_meli = code_meli.get()
        self.gender = gender.get()
        user = User(self.name, self.fname, self.age, self.code_meli, self.gender)
        user.create_user()
        btn.configure(state='disabled')


    def RemoveUser(self, user_name, btn):
        self.user_name = user_name.get()
        remove = UserDB()
        remove.remove_user(self.user_name)
        remove.close()
        btn.configure(state='disabled')
        
    
    def ShowUsers(self):
        users = UserDB()
        result = users.show_users()
        users.close()
        return result


    def SearchUser(self, user_name, frame):
        for widget in frame.winfo_children():
            widget.destroy()

        self.user_name = user_name.get()
        users = UserDB()
        result = users.show_users()
        users.close()

        for user in result:
            if user[3] == self.user_name:
                ansewr = user
                fullname = ctk.CTkLabel(frame, text=f'fullname : {ansewr[0]} {ansewr[1]}')
                fullname.pack(pady=1)
                age = ctk.CTkLabel(frame, text=f'age : {ansewr[2]}')
                age.pack(pady=2)
                username = ctk.CTkLabel(frame, text=f'username : {ansewr[3]}')
                username.pack(pady=2)
                gender = ctk.CTkLabel(frame, text=f'gender : {ansewr[4]}')
                gender.pack(pady=2)
                membership_date = ctk.CTkLabel(frame, text=f'membership-date : {ansewr[5]}\{ansewr[7]}\{ansewr[6]}')
                membership_date.pack(pady=2)
                break
