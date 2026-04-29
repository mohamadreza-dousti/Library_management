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
        self.code = code_meli
    
    def create_admin(self):
        add = AdminDB()
        add.register_admin(self.name, self.fname, self.gender, self.age, self.code, self.user_code, self.password)
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


    def RemoveAdmin(self, code_meli, btn):
        self.code_meli = code_meli.get()
        remove = AdminDB()
        remove.remove_admin(self.code_meli)
        remove.close()
        btn.configure(state='disabled')