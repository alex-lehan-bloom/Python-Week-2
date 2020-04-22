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
