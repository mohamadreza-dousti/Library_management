import customtkinter as ctk
from  tab_veiw.tabs import Main
from Book_anagement.book import BookMnagement as bmng

class Book(Main):
    def __init__(self):
        super().__init__()
        # self.ejra = ejrayi()
        self.make_window()

    def make_window(self):
        add = ctk.CTkButton(self.tab1, text='1.Add book', text_color='gray', command=self.add_book)
        add.pack(pady=10)

        remove = ctk.CTkButton(self.tab1, text='2.Remove book', text_color='gray', command=self.remove_book)
        remove.pack(pady=10)
        
        search = ctk.CTkButton(self.tab1, text='3.Search book', text_color='gray', command=self.search_book)
        search.pack(pady=10)

        show = ctk.CTkButton(self.tab1, text='4.Show book', text_color='gray', command=self.show_books)
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

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back,
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

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back,
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

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back,
                                text_color_disabled='gray')
        bck_btn.pack(pady=2)

    def show_books(self):
        for widget in self.tab1.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab1, text='Show books')
        lable_title.pack(pady=5)

        frame = ctk.CTkFrame(self.tab1, height=20)
        frame.pack(fill='both', expand='True')

        scroll_frame = ctk.CTkScrollableFrame(frame, width=250, height=30)
        scroll_frame.pack(pady=15)
        scroll_frame.grid_columnconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(1, weight=1)
        scroll_frame.grid_columnconfigure(2, weight=1)

        books = bmng()
        result = books.ShowBooks()
        i=0
        for book in result:
            book_title = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'title:{book[0]}')
            book_title.grid(row=i, column=0, pady=5)
            book_author = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'author:{book[1]}')
            book_author.grid(row=i, column=1)
            book_status = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'status:{book[2]}')
            book_status.grid(row=i, column=2)
            i += 1

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back,
                                text_color_disabled='gray')
        bck_btn.pack(pady=5)

    def back(self):
        for widget in self.tab1.winfo_children():
            widget.destroy()
        self.make_window()




# class ejrayi():
#     def save(self, title, author, avalable, save_btn_avalable):
#         save_btn_avalable.configure(state='disabled', fg_color='green',
#                                     text='saved!')
#         self.save = Book()
#         self.save.addBook(title, author, avalable)
        

#     def remove(self, title_rem, remove_btn_avalable):
#         remove_btn_avalable.configure(state='disabled', fg_color='red',
#                                     text='removed!')
#         self.remove = MyApp()
#         self.remove.removeBook(title_rem)
        

#     def search(self, title_ser, scroll_frame, filter, value=2):
#         value = filter.get()
#         for self.widget in scroll_frame.winfo_children():
#             self.widget.destroy()
#         self.search_b = MyApp()
#         self.res = self.search_b.searchBook(title_ser, value)
#         if self.res == []:
#             self.book_lab = ctk.CTkLabel(scroll_frame, text='None', fg_color='black')
#             self.book_lab.pack(pady=20)
#         else:
#             i=0
#             for self.book in self.res:
#                 self.book_title = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'title:{self.book[0]}')
#                 self.book_title.grid(row=i, column=0, pady=5)
#                 self.book_author = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'author:{self.book[1]}')
#                 self.book_author.grid(row=i, column=1)
#                 self.book_status = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'status:{self.book[2]}')
#                 self.book_status.grid(row=i, column=2)
#                 i+=1


#     def show(self, show_btn_avalable, scroll_frame):
#         show_btn_avalable.configure(state='disabled')
#         self.books = MyApp()
#         self.result = self.books.showBooks()
#         for self.book in self.result:
#             self.book_label = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'title:{self.book[0]}  author:{self.book[1]}  status:{self.book[2]}')
#             self.book_label.pack(pady=5)