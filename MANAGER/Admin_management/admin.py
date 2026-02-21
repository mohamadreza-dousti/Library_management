import datetime
from Database.Admin_database import AdminDB

class Admin:
    def __init__(self, name, fname, age, code_meli, gender):
        self.name = name
        self.fname = fname
        self.age = age
        self.user_code = f'a-{code_meli}'
        self.password = f'a{code_meli}'
        self.gender = gender
        self.membership_date = datetime.datetime.now()
        self.year = self.membership_date.year
        self.month = self.membership_date.month
        self.day = self.membership_date.day
    
    def create_admin(self):
        add = AdminDB()
        add.register_admin(self.name, self.fname, self.age, self.user_code, self.password, self.gender, self.year, self.month, self.day)
        add.close()
    
class AdminManagement:
    def __init__(self):
        self.db = AdminDB()
        self.db.create_table()
        self.db.close()
    
    def RegisterAdmin(self, name, fname, age, code_meli, gender, btn):
        self.name = name.get()
        self.fname = fname.get()
        self.age = age.get()
        self.code_meli = code_meli.get()
        self.gender = gender.get()
        admin = Admin(self.name, self.fname, self.age, self.code_meli, self.gender)
        admin.create_admin()
        btn.configure(state='disabled')


    def RemoveAdmin(self, user_name, btn):
        self.user_name = user_name.get()
        remove = AdminDB()
        remove.remove_admin(self.user_name)
        remove.close()
        btn.configure(state='disabled')