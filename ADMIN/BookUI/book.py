import customtkinter as ctk
from ADMIN.Book_anagement.book import BookMnagement as bmng
from Database.Book_database import BookDB, OnlineBookDB
from Database.Post_database import PostDB

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

        online = ctk.CTkButton(self.tab1, text='5.Online reserve', text_color='gray', command=self.online_reserve)
        online.pack(pady=10)

        len_book = ctk.CTkButton(self.tab1, text='6.lend book', text_color='gray', command=self.lending_book)
        len_book.pack(pady=10)

        recive = ctk.CTkButton(self.tab1, text='7.recive book', text_color='gray', command=self.recive_book)
        recive.pack(pady=10)

        exit = ctk.CTkButton(self.tab1, text='Exit', fg_color='blue', text_color='black', command=self.exit, corner_radius=10)
        exit.pack(pady=20)

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

        id = ctk.CTkEntry(self.tab1, placeholder_text='id')
        id.pack(pady=2)

        save_btn_avalable = ctk.CTkButton(self.tab1, text='save', command=lambda:add.AddBook(title, author, id, save_btn_avalable))
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

        id = ctk.CTkEntry(self.tab1, placeholder_text='enter id')
        id.pack(pady=2)

        remove_btn_avalable = ctk.CTkButton(self.tab1, text='remove', command=lambda:remove.RemoveBook(id, remove_btn_avalable))
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

        search_btn_avalable = ctk.CTkButton(self.tab1, text='search', command=lambda:books.SearchBook(title, frame))
        search_btn_avalable.pack()

        frame = ctk.CTkFrame(self.tab1)
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
    
    def online_reserve(self):
        p = PostDB()
        books = OnlineBookDB()
        bmn = bmng()
        get_title = BookDB()

        for widget in self.tab1.winfo_children():
            widget.destroy()

        lable_title = ctk.CTkLabel(self.tab1, text='online reserve')
        lable_title.pack(pady=5)

        res = books.show_books()

        scroll_frame = ctk.CTkScrollableFrame(self.tab1, width=280)
        scroll_frame.pack(pady=15)
        scroll_frame.grid_columnconfigure(0, weight=1)
        scroll_frame.grid_columnconfigure(1, weight=1)
        scroll_frame.grid_columnconfigure(2, weight=1)

        i=0
        code_vars = {}
        menu_vars = {}
        title_vars = {}
        id_vars = {}
        btn_vars = {}
        p_ids = p.get_id()
        p_id_var = ctk.StringVar(value='id')
        option = [f'{i[0]}' for i in p_ids]
        for book in res:
            code_vars[f'code{i}'] = book[4]
            title = get_title.get_title(book[0])[0]
            title_vars[f'book_title{i}'] = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'{title}', width=120)
            title_vars[f'book_title{i}'].grid(row=i, column=0, pady=5)
            id_vars[f'book_id{i}'] = ctk.CTkLabel(scroll_frame, fg_color='black', text=f'{book[0]}', width=25)
            id_vars[f'book_id{i}'].grid(row=i, column=1)
            menu_vars[f'pid{i}'] = ctk.CTkOptionMenu(scroll_frame, values=option, variable=p_id_var, width=35)
            menu_vars[f'pid{i}'].grid(row=i, column=2)
            btn_vars[f'tahvil{i}'] = ctk.CTkButton(scroll_frame, text='Post', width=65,
                                                   command=lambda ctr=i :bmn.Posted(id_vars[f'book_id{ctr}'],
                                                   btn_vars[f'tahvil{ctr}'], title_vars[f'book_title{ctr}'], menu_vars[f'pid{ctr}'], code_vars[f'code{ctr}']))
            btn_vars[f'tahvil{i}'].grid(row=i, column=3)
            i += 1

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back_book,
                                text_color_disabled='gray')
        bck_btn.pack(pady=5)
    
    def lending_book(self):
        lending = bmng()

        for widget in self.tab1.winfo_children():
            widget.destroy()
        
        code_meli_entry = ctk.CTkEntry(self.tab1, placeholder_text='code meli')
        code_meli_entry.pack(pady=5)

        id_entry = ctk.CTkEntry(self.tab1, placeholder_text='id')
        id_entry.pack(pady=5)

        lending_btn = ctk.CTkButton(self.tab1, text='lending', command=lambda:lending.lend_book(code_meli_entry, id_entry, lending_btn))
        lending_btn.pack()

        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back_book,
                                text_color_disabled='gray')
        bck_btn.pack()
    
    def recive_book(self):
        recive = bmng()

        for widget in self.tab1.winfo_children():
            widget.destroy()

        id_entry = ctk.CTkEntry(self.tab1, placeholder_text='id')
        id_entry.pack(pady = 10)
        
        recive_btn = ctk.CTkButton(self.tab1, text='recive', command=lambda:recive.update_status(id_entry, recive_btn))
        recive_btn.pack()
    
        bck_btn = ctk.CTkButton(self.tab1, text='back', command=self.back_book,
                                text_color_disabled='gray')
        bck_btn.pack(pady=5)
    
    def back_book(self):
        for widget in self.tab1.winfo_children():
            widget.destroy()
        self.make_window_book()

    def exit(self):
        for widget in self.tab1.winfo_children():
            widget.destroy()