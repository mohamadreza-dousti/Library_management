import customtkinter as ctk
from ADMIN.BookUI.book import Book
from ADMIN.UserUI.user import User
from MANAGER.AdminUI.admin import Admin
from Database.Admin_database import AdminDB
from Database.User_database import UserDB
from Database.Manager_database import ManagerDB
import threading as trd

class Logs(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.user_entry_admin=None
        self.pass_entry_admin=None
        self.user_entry_manager=None
        self.pass_entry_manager=None


        self.title('CREATED BY DOUSTI')
        self.geometry('520x550')

        self.slidebar = ctk.CTkFrame(self, width=120)
        self.slidebar.pack(side='left')

        self.modir_btn = ctk.CTkButton(self.slidebar, text='Manager', command=self.LogManager)
        self.modir_btn.pack(pady=5)

        self.admin_btn = ctk.CTkButton(self.slidebar, text='Admin', command=self.LogAdmin)
        self.admin_btn.pack(pady=5)

        self.user_btn = ctk.CTkButton(self.slidebar, text='User', command=self.LogUser)
        self.user_btn.pack(pady=5)

        self.main_area = ctk.CTkFrame(self)
        self.main_area.pack(side='right', expand='True', fill='both')

    def LogManager(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()

        self.lable = ctk.CTkLabel(self.main_area, text='MANAGER')
        self.lable.pack()

        self.user_entry_manager = ctk.CTkEntry(self.main_area, placeholder_text='user name')
        self.user_entry_manager.pack(pady = 5, fill='both')

        self.pass_entry_manager = ctk.CTkEntry(self.main_area, placeholder_text='password')
        self.pass_entry_manager.pack(pady = 5, fill='both')

        login = ctk.CTkButton(self.main_area, text='login', fg_color='white', text_color='black', command=self.manager_widgets)
        login.pack(pady=15, fill='both')
    
    def LogAdmin(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
    
        self.lable = ctk.CTkLabel(self.main_area, text='ADMIN')
        self.lable.pack()
    
        self.user_entry_admin = ctk.CTkEntry(self.main_area, placeholder_text='user name')
        self.user_entry_admin.pack(pady = 5, fill='both')

        self.pass_entry_admin = ctk.CTkEntry(self.main_area, placeholder_text='password')
        self.pass_entry_admin.pack(pady = 5, fill='both')

        login = ctk.CTkButton(self.main_area, text='login', fg_color='white', text_color='black', command=self.admin_widgets)
        login.pack(pady = 15, fill='both')
    
    def LogUser(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
        
        self.lable = ctk.CTkLabel(self.main_area, text='USER')
        self.lable.pack()

    def manager_widgets(self):
        username = self.user_entry_manager.get()
        password = self.pass_entry_manager.get()
        manager_db = ManagerDB()
        manager_db.create_table()
        pas = manager_db.get_pass_manager(username)
        manager_db.close()
        if pas:
            if pas[0] == password:
                for widget in self.main_area.winfo_children():
                    widget.destroy()

                admin_widgets = Admin(self.main_area)
                admin_widgets.make_window_admin()
            else:
                wrong = ctk.CTkLabel(self.main_area, text='password or username is incorrect')
                wrong.pack()
        else:
            wrong = ctk.CTkLabel(self.main_area, text='password or username is incorrect')
            wrong.pack()

    def admin_widgets(self):
        username = self.user_entry_admin.get()
        password = self.pass_entry_admin.get()
        admin_db = AdminDB()
        admin_db.create_table()
        pas = admin_db.get_pass_admin(username)
        admin_db.close()
        if pas:
            if pas[0] == password:
                for widget in self.main_area.winfo_children():
                    widget.destroy()
                self.tabview = ctk.CTkTabview(self.main_area, width=380, height=230,
                                        corner_radius=15)
                self.tabview.pack(padx=10, pady=10, fill='both',
                            expand=True)

                self.tab1 = self.tabview.add('Books')
                self.tab2 = self.tabview.add('Users')
                book_widgets = Book(self.tab1)
                user_widgets = User(self.tab2)
                book_trd = trd.Thread(target=book_widgets.make_window_book(), name='book-widgets')
                user_trd = trd.Thread(target=user_widgets.make_window_user(), name='user-widgets')
                book_trd.start()
                user_trd.start()
            
            else:
                wrong = ctk.CTkLabel(self.main_area, text='password or username is incorrect')
                wrong.pack()
        else:
            wrong = ctk.CTkLabel(self.main_area, text='password or username is incorrect')
            wrong.pack()