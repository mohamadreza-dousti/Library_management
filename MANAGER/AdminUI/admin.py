import customtkinter as ctk
from MANAGER.Admin_management.admin import AdminManagement as amng

class Admin:
    def __init__(self, tab1):
        self.tab1 = tab1

    def make_window_admin(self):
        add_admin = ctk.CTkButton(self.tab1, text='Register Admin', command=self.add_admin)
        add_admin.pack(pady=5)

        remove_admin = ctk.CTkButton(self.tab1, text='Remove Admin', command=self.remove_admin)
        remove_admin.pack(pady=5)

        exit = ctk.CTkButton(self.tab1, text='Exit', fg_color='blue', text_color='black', command=self.exit, corner_radius=10)
        exit.pack(pady=20)

    def add_admin(self):
        add = amng()
    
        for widget in self.tab1.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab1, text='Register admin')
        lable_title.pack(pady=5, fill='both')

        name = ctk.CTkEntry(self.tab1, placeholder_text='name')
        name.pack(pady=2)

        f_name = ctk.CTkEntry(self.tab1, placeholder_text='f-name')
        f_name.pack(pady=2)

        age = ctk.CTkEntry(self.tab1, placeholder_text='age')
        age.pack(pady=2)

        code = ctk.CTkEntry(self.tab1, placeholder_text='code meli')
        code.pack(pady=2)

        values = ['male', 'female', 'other']
        option_var = ctk.StringVar(value='gender')
        gender = ctk.CTkOptionMenu(self.tab1, values=values, variable=option_var)
        gender.pack(pady=2)

        save_btn_avalable = ctk.CTkButton(self.tab1, text='save', command=lambda:add.RegisterAdmin(name, f_name, age, code, gender, save_btn_avalable))
        save_btn_avalable.pack(pady=5)

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back_admin,
                                text_color_disabled='gray')
        bck_btn.pack()

    def remove_admin(self):
        remove = amng()

        for widget in self.tab1.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab1, text='Remove admin')
        lable_title.pack(pady=5)

        code_meli = ctk.CTkEntry(self.tab1, placeholder_text='code meli')
        code_meli.pack(pady=2)

        remove_btn_avalable = ctk.CTkButton(self.tab1, text='remove', command=lambda:remove.RemoveAdmin(code_meli, remove_btn_avalable))
        remove_btn_avalable.pack(pady=5)

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back_admin,
                                text_color_disabled='gray')
        bck_btn.pack()


    def back_admin(self):
        for widget in self.tab1.winfo_children():
            widget.destroy()
        self.make_window_admin()

    def exit(self):
        for widget in self.tab1.winfo_children():
            widget.destroy()
