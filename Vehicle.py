from FileHandler import FileHandler
from datetime import datetime



class Vehicle:
    vehicles_db = FileHandler()
    vehicles = vehicles_db.load_from_csv('csv_files/Vehicles.csv')

    def __init__(self, path_to_vehicles_db):
        self.path_to_vehicles_db = path_to_vehicles_db

    def update_vehicle_with_id(self, id, **kwargs):
        return self.vehicles_db.update_csv(self.path_to_vehicles_db, id, kwargs)

    def get_car_by_features(self, and_or='and', **kwargs):
        return self.vehicles_db.get_rows_matching_search_criteria(self.path_to_vehicles_db, kwargs, and_or)

    def get_time_to_test(self, id):
        car_matching_id = []
        for car in self.vehicles:
            if car['id'] == id:
                car_matching_id = car
        if len(car_matching_id) == 0:
            return False
        else:
            previous_test_date = car_matching_id['last_test']
            previous_test_date = datetime.strptime(previous_test_date, "%d-%m-%Y")
            days_since_last_test = datetime.now() - previous_test_date
            days_until_next_test = 180 - days_since_last_test.days
            if days_until_next_test > 0:
                print("You have {} days until your next test.".format(days_until_next_test))
            else:
                print("You are overdue for your test by {} days.".format(days_until_next_test * -1))
            return days_until_next_test
