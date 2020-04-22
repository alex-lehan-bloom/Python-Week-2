from FileHandler import FileHandler


class User():
    user_db = FileHandler()

    def __init__(self, path_to_database):
        self.path_to_database = path_to_database
        self.users = self.user_db.load_from_csv(self.path_to_database)

    def user_auth(self, name, password):
        try:
            self.validate_argument_is_string(name, password)
        except Exception as e:
            print("Error: The 'user_auth' function only accepts strings as arguments.")
            exit()
        user_exists = False
        for row in self.users:
            username_from_db = "{} {}".format(row['first'],row['last'])
            if username_from_db.lower() == name.lower() and row['password'] == password:
                user_exists = row['role']
        return user_exists

    def add_user(self, **kwargs):
        return self.user_db.append_to_csv(self.path_to_database, kwargs)

    def validate_argument_is_string(self, *args):
        for argument in args:
            if not isinstance(argument, str):
                raise Exception()


user1 = User("csv_files/User.csv")
# exists = user1.user_auth("alex bloom", "passwd123")
# print(exists)
print(user1.add_user(first="Amir",last="Bernstein",password="cats1234",position="Teacher",salary=200000 ,role="Admin"))
