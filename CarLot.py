from FileHandler import FileHandler
from Logger import Logger

logger = Logger("logs", "log_file.txt")
vehicles_db = FileHandler()
user_db = FileHandler()


class CarLot:

    def add_to_fleet(self, vehicle):
        # vehicles = vehicles_db.load_from_csv("csv_files/Vehicles.csv")
        add_vehicle = vehicles_db.append_to_csv("csv_files//Vehicles.csv", vehicle)
        if add_vehicle == True:
            logger.add_to_log("New vehicle added to Vehicle.csv")
            print("The vehicle was successfully added.")
            return True
        else:
            False

    def get_fleet_size(self):
        size = vehicles_db.get_num_rows("csv_files/Vehicles.csv")
        if size == False:
            return False
        else:
            print("The size of the fleet is {}".format(size))
            return True

    def get_fleet_size_by_brand(self, brand):
        count = vehicles_db.get_num_rows_matching_search_criteria("csv_files/Vehicles.csv", 'brand', brand)
        return count

    def get_cars_by_filter(self,and_or='and',**kwargs):

        pass

    def update_salary_by_name(self, csv_file, name, new_salary):
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

    def people_who_own_more_than_one_car(self):
        vehicles = vehicles_db.load_from_csv("csv_files/Vehicles.csv")
        vehicles = [car for car in vehicles ]
        users_with_multiple_cars = []
        for car_one in vehicles:
            count = 0
            for car_two in vehicles:
                print(car_one['owner'])
                print(car_two['owner'])
                if car_one['owner'].lower() == car_two['owner'].lower():
                    count += 1
            if count >= 2:
                users_with_multiple_cars.append(car_one)
        users_with_multiple_cars = sorted(users_with_multiple_cars, key=lambda row: row['owner'])
        for i in users_with_multiple_cars:
            print(i)
        if len(users_with_multiple_cars) > 0:
            return users_with_multiple_cars
        else:
            return False

    def employees_with_cars(self):
        users = user_db.load_from_csv("csv_files/User.csv")
        users = [user for user in users]
        vehicles = vehicles_db.load_from_csv("csv_files/Vehicles.csv")
        vehicles = [car for car in vehicles]
        employees_with_cars = []
        for car in vehicles:
            for user in users:
                username = "{} {}".format(user['first'], user['last'])
                if username.lower() == car['owner'].lower():
                    employees_with_cars.append(username)
        employees_with_cars = list(dict.fromkeys(employees_with_cars))
        if len(employees_with_cars) > 0:
            return employees_with_cars
        else:
            return False


