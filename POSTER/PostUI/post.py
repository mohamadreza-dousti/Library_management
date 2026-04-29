from Database.Book_database import PostBookDB
from POSTER.PostProfile.post import PostProfileManagement as ppm
from Database.Post_database import PostDB
from Database.User_database import UserDB
import customtkinter as ctk

class PostProfile:
    def __init__(self, main_area, username):
        pid = PostDB()
        self.main_area = main_area
        self.username = username
        self.id = pid.get_id_person(self.username)[0]

    def make_window_post_profile(self):
        p = ppm()
        udb = UserDB()
        for widget in self.main_area.winfo_children():
            widget.destroy()
        
        db = PostBookDB()
        res = db.show_books(self.id)
        scroll_vertical = ctk.CTkScrollableFrame(self.main_area, width=350, height=230, orientation='vertical')
        scroll_vertical.pack()

        scroll = ctk.CTkScrollableFrame(scroll_vertical, orientation='horizontal')
        scroll.pack(fill='both', expand=True)

        scroll.columnconfigure(0, weight=1)
        scroll.columnconfigure(1, weight=1)
        scroll.columnconfigure(2, weight=1)
        scroll.columnconfigure(3, weight=1)
        scroll.columnconfigure(4, weight=1)

        i=0
        title_vars = {}
        fname_vars = {}
        phone_vars = {}
        address_vars = {}
        btn_vars = {}
        code_vars = {}
        id_vars = {}
        for book in res:
            fname = udb.get_fname(f'u-{book[7]}')
            phone = udb.get_phone(f'u-{book[7]}')
            address = udb.get_address(f'u-{book[7]}')

            code_vars[f'code{i}'] = book[7]
            id_vars[f'id{i}'] = book[2]

            title_vars[f'title{i}'] = ctk.CTkLabel(scroll, text=f'title:{book[1]}', width=50)
            title_vars[f'title{i}'].grid(row=i, column=0)

            fname_vars[f'f_name{i}'] = ctk.CTkLabel(scroll, text=fname, width=50)
            fname_vars[f'f_name{i}'].grid(row=i, column=1)

            phone_vars[f'phone_number{i}'] = ctk.CTkLabel(scroll, text=phone, width=50)
            phone_vars[f'phone_number{i}'].grid(row=i, column=2)

            address_vars[f'user_address{i}'] = ctk.CTkLabel(scroll, text=address)
            address_vars[f'user_address{i}'].grid(row=i, column=3, padx=5)

            btn_vars[f'tahvil{i}'] = ctk.CTkButton(scroll, text='tahvil', command=lambda ctr=i : p.tahvil(code_vars[f'code{ctr}'], id_vars[f'id{ctr}'], btn_vars[f'tahvil{ctr}']), width=50)
            btn_vars[f'tahvil{i}'].grid(row=i, column=4)

            i+=1
        
        refresh = ctk.CTkButton(self.main_area, text='refresh', fg_color='blue', text_color='black', command=self.refresh, corner_radius=10)
        refresh.pack(pady=10)

        exit = ctk.CTkButton(self.main_area, text='Exit', fg_color='blue', text_color='black', command=self.exit, corner_radius=10)
        exit.pack(pady=10)


    def refresh(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
        self.make_window_post_profile()


    def exit(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
    