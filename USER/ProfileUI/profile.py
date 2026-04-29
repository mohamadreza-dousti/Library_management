import customtkinter as ctk
from USER.Profile_management.profile import ProfileManagement as pmng
from USER.reserve.book import reserveBook as rb

class Profile:
    def __init__(self, main_area, username):
        self.main_area = main_area
        self.username = username

    def make_window_profile(self):
        manage = pmng(self.username)
        for widget in self.main_area.winfo_children():
            widget.destroy()
        
        self.main_area.grid_columnconfigure(0, weight=1)
        self.main_area.grid_columnconfigure(1, weight=1)
        
        name = ctk.CTkLabel(self.main_area, text='name', bg_color='gray', text_color='black', corner_radius=2, width=200)
        name.grid(row=0, column=0, pady=5)
        name_value = manage.GetName()
        name_value = name_value[0]
        name_val = ctk.CTkLabel(self.main_area, text=name_value, bg_color='gray', text_color='black', corner_radius=2, width=200)
        name_val.grid(row=0, column=1, pady=5)

        fname = ctk.CTkLabel(self.main_area, text='family-name', bg_color='gray', text_color='black', corner_radius=2, width=200)
        fname.grid(row=1, column=0, pady=5)
        fname_value = manage.GetFname()
        fname_value = fname_value[0]
        fname_val = ctk.CTkLabel(self.main_area, text=fname_value, bg_color='gray', text_color='black', corner_radius=2, width=200)
        fname_val.grid(row=1, column=1, pady=5)

        age = ctk.CTkLabel(self.main_area, text='age', bg_color='gray', text_color='black', corner_radius=2, width=200)
        age.grid(row=2, column=0, pady=5)
        age_value = manage.GetAge()
        age_value = age_value[0]
        age_val = ctk.CTkLabel(self.main_area, text=age_value, bg_color='gray', text_color='black', corner_radius=2, width=200)
        age_val.grid(row=2, column=1, pady=5)

        gender = ctk.CTkLabel(self.main_area, text='gender', bg_color='gray', text_color='black', corner_radius=2, width=200)
        gender.grid(row=3, column=0, pady=5)
        gender_value = manage.GetGender()
        gender_value = gender_value[0]
        gender_val = ctk.CTkLabel(self.main_area, text=gender_value, bg_color='gray', text_color='black', corner_radius=2, width=200)
        gender_val.grid(row=3, column=1, pady=5)

        membership_date = ctk.CTkLabel(self.main_area, text='membership-date', bg_color='gray', text_color='black', corner_radius=2, width=200)
        membership_date.grid(row=4, column=0, pady=5)
        membership_date_value = manage.GetMembershipDate()
        membership_date_val = ctk.CTkLabel(self.main_area, text=membership_date_value, bg_color='gray', text_color='black', corner_radius=2, width=200)
        membership_date_val.grid(row=4, column=1, pady=5)

        expire_date = ctk.CTkLabel(self.main_area, text='expire-date', bg_color='gray', text_color='black', corner_radius=2, width=200)
        expire_date.grid(row=5, column=0, pady=5)
        expire_date_value = manage.GetExpireDate()
        expire_date_val = ctk.CTkLabel(self.main_area, text=expire_date_value, bg_color='gray', text_color='black', corner_radius=2, width=200)
        expire_date_val.grid(row=5, column=1, pady=5)

        reserve_book = ctk.CTkButton(self.main_area, text='reserve book', fg_color='blue', text_color='white', corner_radius=10, command=self.search)
        reserve_book.grid(row=6, column=0, columnspan=2, pady=10)

        exit = ctk.CTkButton(self.main_area, text='Exit', fg_color='red', text_color='black', command=self.exit, corner_radius=10)
        exit.grid(row=8, column=0, columnspan=2, pady=40)


    def exit(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
    
    def search(self):
        search = rb(self.username)
        self.exit()

        title = ctk.CTkEntry(self.main_area, placeholder_text='search book')
        title.pack(pady=2)

        search_btn_avalable = ctk.CTkButton(self.main_area, text='search', command=lambda:search.search_book_user(title, scroll_frame))
        search_btn_avalable.pack()

        scroll_frame = ctk.CTkScrollableFrame(self.main_area, height=300, width=300)
        scroll_frame.pack(pady=5)
        scroll_frame.grid_columnconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(1, weight=1)
        scroll_frame.grid_columnconfigure(2, weight=1)

        exit_search = ctk.CTkButton(self.main_area, text='Exit', fg_color='red', text_color='black', command=self.exit_search, corner_radius=10)
        exit_search.pack(pady=40)
    
    def exit_search(self):
        for widget in self.main_area.winfo_children():
            widget.destroy()
        self.make_window_profile()