from FileHandler import FileHandler

class User:
    def user_auth(self, name, password):
        try:
            self.validate_argument_is_string(name, password)
        except Exception as e:
            print("Error: The 'user_auth' function only accepts strings as arguments.")
            exit()
        user_db = FileHandler()
        users = user_db.load_from_csv("csv_files/User.csv")
        user_name = name.split()
        user_exists = False
        for row in users:
            if row['first'].lower() == user_name[0].lower() and row['last'].lower() == user_name[1].lower() and row['password'] == password:
                user_exists = row['role']
        return user_exists


    def validate_argument_is_string(self, *args):
        for argument in args:
            if not isinstance(argument, str):
                raise Exception()


user1 = User()
exists = user1.user_auth("alex dames", "passwd123")
print(exists)


