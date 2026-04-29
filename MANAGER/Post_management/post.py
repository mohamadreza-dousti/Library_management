from Database.Post_database import PostDB

class Post:
    def __init__(self, name, fname, age, code_meli, gender, id):
        self.name = name
        self.fname = fname
        self.age = age
        self.user_code = f'p-{code_meli}'
        self.password = f'p{code_meli}'
        self.gender = gender
        self.code = code_meli
        self.id = id
    
    def create_post(self):
        add = PostDB()
        add.register_post(self.name, self.fname, self.age, self.code, self.user_code, self.password, self.gender, self.id)
        add.close()
    
class PostManagement:
    def __init__(self):
        self.db = PostDB()
        self.db.create_table()
        self.db.close()
    
    def RegisterPost(self, name, fname, age, code_meli, gender, id, btn):
        self.name = name.get()
        self.fname = fname.get()
        self.age = age.get()
        self.code_meli = code_meli.get()
        self.gender = gender.get()
        self.id = id.get()
        post = Post(self.name, self.fname, self.age, self.code_meli, self.gender, self.id)
        post.create_post()
        btn.configure(state='disabled')


    def RemovePost(self, user_name, btn):
        self.user_name = user_name.get()
        remove = PostDB()
        remove.remove_post(self.user_name)
        remove.close()
        btn.configure(state='disabled')