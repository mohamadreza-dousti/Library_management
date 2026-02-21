import customtkinter as ctk
from Book_anagement.book import BookMnagement as bmng

class Book:
    def __init__(self, tab1):
        self.tab1 = tab1

    def make_window_book(self):
        for widget in self.tab1.winfo_children():
            widget.destroy()

        add = ctk.CTkButton(self.tab1, text='1.Add book', text_color='gray', command=self.add_book)
        add.pack(pady=10)

        remove = ctk.CTkButton(self.tab1, text='2.Remove book', text_color='gray', command=self.remove_book)
        remove.pack(pady=10)
        
        search = ctk.CTkButton(self.tab1, text='3.Search book', text_color='gray', command=self.search_book)
        search.pack(pady=10)

        show = ctk.CTkButton(self.tab1, text='4.Show books', text_color='gray', command=self.show_books)
        show.pack(pady=10)

    def add_book(self):
        add = bmng()
    
        for widget in self.tab1.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab1, text='Add book')
        lable_title.pack(pady=5, fill='both')

        title = ctk.CTkEntry(self.tab1, placeholder_text='title')
        title.pack(pady=2)

        author = ctk.CTkEntry(self.tab1, placeholder_text='author')
        author.pack(pady=2)

        avalable = ctk.CTkEntry(self.tab1, placeholder_text='avalable')
        avalable.pack(pady=2)

        save_btn_avalable = ctk.CTkButton(self.tab1, text='save', command=lambda:add.AddBook(title, author, avalable, save_btn_avalable))
        save_btn_avalable.pack(pady=5)

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back_book,
                                text_color_disabled='gray')
        bck_btn.pack()

    def remove_book(self):
        remove = bmng()

        for widget in self.tab1.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab1, text='Remove book')
        lable_title.pack(pady=5)

        title = ctk.CTkEntry(self.tab1, placeholder_text='enter title')
        title.pack(pady=2)

        remove_btn_avalable = ctk.CTkButton(self.tab1, text='remove', command=lambda:remove.RemoveBook(title, remove_btn_avalable))
        remove_btn_avalable.pack(pady=5)

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back_book,
                                text_color_disabled='gray')
        bck_btn.pack()


    def search_book(self):
        books = bmng()

        for widget in self.tab1.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab1, text='Search book')
        lable_title.pack(pady=5)

        title = ctk.CTkEntry(self.tab1, placeholder_text='enter title')
        title.pack(pady=2)

        option = ['1', '0', 'both']
        filter_var = ctk.StringVar(value='status')
        filter = ctk.CTkOptionMenu(self.tab1, values=option, variable=filter_var)
        filter.pack(pady=3)

        search_btn_avalable = ctk.CTkButton(self.tab1, text='search', command=lambda:books.SearchBook(title, filter, frame))
        search_btn_avalable.pack()

        frame = ctk.CTkFrame(self.tab1, height=20)
        frame.pack(fill='both', expand='True')

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back_book,
                                text_color_disabled='gray')
        bck_btn.pack(pady=2)

    def show_books(self):
        books = bmng()

        for widget in self.tab1.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab1, text='Show books')
        lable_title.pack(pady=5)

        option = ['1', '0', 'both']
        filter_var = ctk.StringVar(value='status')
        filter = ctk.CTkOptionMenu(self.tab1, values=option, variable=filter_var)
        filter.pack(pady=3)

        show_btn_avalable = ctk.CTkButton(self.tab1, text='show', command=lambda:books.ShowBooks(filter, frame))
        show_btn_avalable.pack()

        frame = ctk.CTkFrame(self.tab1, height=20)
        frame.pack(fill='both', expand='True')

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back_book,
                                text_color_disabled='gray')
        bck_btn.pack(pady=5)
    
    def back_book(self):
        for widget in self.tab1.winfo_children():
            widget.destroy()
        self.make_window_book()