from FileHandler import FileHandler

class CarLot:
    def add_to_fleet(self, vehicle):
        vehicles_db = FileHandler()
        # vehicles = vehicles_db.load_from_csv("csv_files/Vehicles.csv")
        add_vehicle = vehicles_db.append_to_csv("csv_files//Vehicles.csv", vehicle)
        if add_vehicle == True:
            print("The vehicle was successfully added.")
            return True
        else:
            False


    def update_salary_by_name(self, csv_file, name, new_salary):
        user_db = FileHandler()
        users = user_db.load_from_csv(csv_file)
        user_exists = False
        user_id = None
        updated_user_info = None
        for user in users:
            if "{} {}".format(user['first'], user['last']) == name:
                user_exists = True
                updated_user_info = user
                updated_user_info['salary'] = new_salary
                user_id = user["user_id"]
        if user_exists == False:
            print("Error: User could not be found.")
            return False
        else:
            user_db.update_csv(csv_file, user_id, updated_user_info)
            print("Salary for {} was successfully updated.".format(name))
            return True

my_car_lot = CarLot()
# my_car_lot.update_salary_by_name("csv_files/User.csv", "Alex Bloom", 8000)
vehicle_to_add = {'owner': 'Ruthy Lewis','brand': 'Toyota','color': 'Yellow','door_count': 4,'last_test': '5-07-1992'}
my_car_lot.add_to_fleet(vehicle_to_add)

