from Database.User_database import UserDB

class ProfileManagement:
    def __init__(self, username):
        self.username = username
        self.db = UserDB()
        self.db.create_table()
        self.db.close()
    
    def GetName(self):
        getName = UserDB()
        name = getName.get_name(self.username)
        getName.close()
        return name

    def GetFname(self):
        getFname = UserDB()
        fname = getFname.get_fname(self.username)
        getFname.close()
        return fname

    def GetAge(self):
        getAge = UserDB()
        age = getAge.get_age(self.username)
        getAge.close()
        return age

    def GetGender(self):
        getGender = UserDB()
        gender = getGender.get_gender(self.username)
        getGender.close()
        return gender

    def GetMembershipDate(self):
        getMembershipDate = UserDB()
        year, month, day = getMembershipDate.get_membership_date(self.username)
        getMembershipDate.close()
        return f'{year}\\{month}\\{day}'
    
    def GetExpireDate(self):
        getExpireDate = UserDB()
        year, month, day = getExpireDate.get_expire_date(self.username)
        getExpireDate.close()
        return f'{year}\\{month}\\{day}'