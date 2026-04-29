from Database.Post_database import PostDB
from Database.Book_database import PostBookDB
from Database.Book_database import TrustDB
from Database.User_database import UserDB
from datetime import datetime

class PostProfileManagement:
    def __init__(self):
        pass
    def tahvil(self, code, id, btn):
        now = datetime.now()
        month = now.month
        day = now.day
        pbook = PostBookDB()
        tbook = TrustDB()
        udb = UserDB()
        name = udb.get_name(f'u-{code}')[0]
        fname = udb.get_fname(f'u-{code}')[0]
        phone = udb.get_phone(f'u-{code}')[0]
        username = f'u-{code}'
        tbook.add_book(name, fname, phone, month+1, day, id, username)
        pbook.update_arrive(id)
        btn.configure(state='disabled')

