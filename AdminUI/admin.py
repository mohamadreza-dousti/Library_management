import customtkinter as ctk
from Admin_management.admin import AdminManagement as amng

class Admin:
    def __init__(self, main_area):
        self.main_area = main_area

    def make_window_admin(self):
        add_admin = ctk.CTkButton(self.main_area, text='Register Admin', command=self.add_admin)
        add_admin.pack(pady=5)

        remove_admin = ctk.CTkButton(self.main_area, text='Remove Admin', command=self.remove_admin)
        remove_admin.pack(pady=5)

    def add_admin(self):
        add = amng()
    
        for widget in self.main_area.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.main_area, text='Register admin')
        lable_title.pack(pady=5, fill='both')

        name = ctk.CTkEntry(self.main_area, placeholder_text='name')
        name.pack(pady=2)

        f_name = ctk.CTkEntry(self.main_area, placeholder_text='f-name')
        f_name.pack(pady=2)

        age = ctk.CTkEntry(self.main_area, placeholder_text='age')
        age.pack(pady=2)

        code = ctk.CTkEntry(self.main_area, placeholder_text='code meli')
        code.pack(pady=2)

        values = ['male', 'female', 'other']
        option_var = ctk.StringVar(value='gender')
        gender = ctk.CTkOptionMenu(self.main_area, values=values, variable=option_var)
        gender.pack(pady=2)

        save_btn_avalable = ctk.CTkButton(self.main_area, text='save', command=lambda:add.RegisterAdmin(name, f_name, age, code, gender, save_btn_avalable))
        save_btn_avalable.pack(pady=5)

        bck_btn = ctk.CTkButton(self.main_area, text='back', command=self.back_admin,
                                text_color_disabled='gray')
        bck_btn.pack()

    def remove_admin(self):
        remove = amng()

        for widget in self.main_area.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.main_area, text='Remove admin')
        lable_title.pack(pady=5)

        user_name = ctk.CTkEntry(self.main_area, placeholder_text='username')
        user_name.pack(pady=2)

        remove_btn_avalable = ctk.CTkButton(self.main_area, text='remove', command=lambda:remove.RemoveAdmin(user_name, remove_btn_avalable))
        remove_btn_avalable.pack(pady=5)

        bck_btn = ctk.CTkButton(self.main_area, text='back', command=self.back_admin,
                                text_color_disabled='gray')
        bck_btn.pack()


    def back_admin(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
        self.make_window_admin()
