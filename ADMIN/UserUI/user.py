import customtkinter as ctk
from ADMIN.User_management.user import UserManagement as umng

class User:
    def __init__(self, tab2):
        self.tab2 = tab2
    
    def make_window_user(self):
        for widget in self.tab2.winfo_children():
            widget.destroy()

        add = ctk.CTkButton(self.tab2, text='1.Add user', text_color='gray', command=self.add_user)
        add.pack(pady=10)

        remove = ctk.CTkButton(self.tab2, text='2.Remove user', text_color='gray', command=self.remove_user)
        remove.pack(pady=10)
        
        search = ctk.CTkButton(self.tab2, text='3.Search user', text_color='gray', command=self.search_user)
        search.pack(pady=10)

        show = ctk.CTkButton(self.tab2, text='4.Show users', text_color='gray', command=self.show_users)
        show.pack(pady=10)
    
    def add_user(self):
        add = umng()
    
        for widget in self.tab2.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab2, text='Register user')
        lable_title.pack(pady=5, fill='both')

        name = ctk.CTkEntry(self.tab2, placeholder_text='name')
        name.pack(pady=2)

        f_name = ctk.CTkEntry(self.tab2, placeholder_text='f-name')
        f_name.pack(pady=2)

        age = ctk.CTkEntry(self.tab2, placeholder_text='age')
        age.pack(pady=2)

        code = ctk.CTkEntry(self.tab2, placeholder_text='code meli')
        code.pack(pady=2)

        values = ['male', 'female', 'other']
        option_var = ctk.StringVar(value='gender')
        gender = ctk.CTkOptionMenu(self.tab2, values=values, variable=option_var)
        gender.pack(pady=2)

        save_btn_avalable = ctk.CTkButton(self.tab2, text='save', command=lambda:add.AddUser(name, f_name, age, code, gender, save_btn_avalable))
        save_btn_avalable.pack(pady=5)

        bck_btn = ctk.CTkButton(self.tab2, text='back', command=self.back_user,
                                text_color_disabled='gray')
        bck_btn.pack()

    def remove_user(self):
        remove = umng()

        for widget in self.tab2.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab2, text='Remove user')
        lable_title.pack(pady=5)

        user_name = ctk.CTkEntry(self.tab2, placeholder_text='username')
        user_name.pack(pady=2)

        remove_btn_avalable = ctk.CTkButton(self.tab2, text='remove', command=lambda:remove.RemoveUser(user_name, remove_btn_avalable))
        remove_btn_avalable.pack(pady=5)

        bck_btn = ctk.CTkButton(self.tab2, text='back', command=self.back_user,
                                text_color_disabled='gray')
        bck_btn.pack()


    def search_user(self):
        users = umng()

        for widget in self.tab2.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab2, text='Search user')
        lable_title.pack(pady=5)

        user_name = ctk.CTkEntry(self.tab2, placeholder_text='username')
        user_name.pack(pady=2)

        search_btn_avalable = ctk.CTkButton(self.tab2, text='search', command=lambda:users.SearchUser(user_name, frame))
        search_btn_avalable.pack()

        frame = ctk.CTkFrame(self.tab2, height=20)
        frame.pack(fill='both', expand='True')

        bck_btn = ctk.CTkButton(self.tab2, text='back', command=self.back_user,
                                text_color_disabled='gray')
        bck_btn.pack(pady=2)

    def show_users(self):
        for widget in self.tab2.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab2, text='Show users')
        lable_title.pack(pady=5)

        frame = ctk.CTkFrame(self.tab2, width=350)
        frame.pack(fill='both', expand='True')

        scroll_frame = ctk.CTkScrollableFrame(frame, width=280)
        scroll_frame.pack(expand='True')
        scroll_frame.grid_columnconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(1, weight=1)

        users = umng()
        result = users.ShowUsers()
        i=0
        for user in result:
            full_name = ctk.CTkLabel(scroll_frame, fg_color='white', text_color='black', text=f'fullname : {user[0]} {user[1]}')
            full_name.grid(row=i, column=0, pady=1)
            i += 1
            date_of_membership = ctk.CTkLabel(scroll_frame, fg_color='white', text_color='black', text=f'membership date : {user[5]}\{user[7]}\{user[6]}')
            date_of_membership.grid(row=i, column=0)
            i += 1
            end = ctk.CTkLabel(scroll_frame, fg_color='black', text_color='black', text=' ', width=280)
            end.grid(row=i, column=0)
            i += 1

        bck_btn = ctk.CTkButton(self.tab2, text='back', command=self.back_user,
                                text_color_disabled='gray')
        bck_btn.pack(pady=5)

    def back_user(self):
        for widget in self.tab2.winfo_children():
            widget.destroy()
        self.make_window_user()