import customtkinter as ctk
from MANAGER.Post_management.post import PostManagement as pmng

class Post:
    def __init__(self, tab2):
        self.tab2 = tab2

    def make_window_post(self):
        add_admin = ctk.CTkButton(self.tab2, text='Register post', command=self.add_post)
        add_admin.pack(pady=5)

        remove_admin = ctk.CTkButton(self.tab2, text='Remove post', command=self.remove_post)
        remove_admin.pack(pady=5)

        exit = ctk.CTkButton(self.tab2, text='Exit', fg_color='blue', text_color='black', command=self.exit, corner_radius=10)
        exit.pack(pady=20)

    def add_post(self):
        add = pmng()
    
        for widget in self.tab2.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab2, text='Register post')
        lable_title.pack(pady=5, fill='both')

        name = ctk.CTkEntry(self.tab2, placeholder_text='name')
        name.pack(pady=2)

        f_name = ctk.CTkEntry(self.tab2, placeholder_text='f-name')
        f_name.pack(pady=2)

        age = ctk.CTkEntry(self.tab2, placeholder_text='age')
        age.pack(pady=2)

        code = ctk.CTkEntry(self.tab2, placeholder_text='code meli')
        code.pack(pady=2)

        id = ctk.CTkEntry(self.tab2, placeholder_text='id')
        id.pack(pady=2)

        values = ['male', 'female', 'other']
        option_var = ctk.StringVar(value='gender')
        gender = ctk.CTkOptionMenu(self.tab2, values=values, variable=option_var)
        gender.pack(pady=2)

        save_btn_avalable = ctk.CTkButton(self.tab2, text='save', command=lambda:add.RegisterPost(name, f_name, age, code, gender, id, save_btn_avalable))
        save_btn_avalable.pack(pady=5)

        bck_btn = ctk.CTkButton(self.tab2, text='back', command=self.back_post,
                                text_color_disabled='gray')
        bck_btn.pack()

    def remove_post(self):
        remove = pmng()

        for widget in self.tab2.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab2, text='Remove post')
        lable_title.pack(pady=5)

        code_meli = ctk.CTkEntry(self.tab2, placeholder_text='code meli')
        code_meli.pack(pady=2)

        remove_btn_avalable = ctk.CTkButton(self.tab2, text='remove', command=lambda:remove.RemovePost(code_meli, remove_btn_avalable))
        remove_btn_avalable.pack(pady=5)

        bck_btn = ctk.CTkButton(self.tab2, text='back', command=self.back_post,
                                text_color_disabled='gray')
        bck_btn.pack()


    def back_post(self):
        for widget in self.tab2.winfo_children():
            widget.destroy()
        self.make_window_post()

    def exit(self):
        for widget in self.tab2.winfo_children():
            widget.destroy()
