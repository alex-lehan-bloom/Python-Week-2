from FileHandler import FileHandler
from Logger import Logger
from Vehicle import Vehicle
from CarLot import CarLot
from datetime import datetime


# FILEHANDLER
# new_row = {'first': "New_first_name", 'last': "new_last_name"}
# my_file_handler = FileHandler()
# # field_names = get_csv_headers("csv_files/Test.csv")
# # # print(my_file_handler.remove_from_csv("csv_files/Test.csv", '2'))
# # my_file_handler.update_csv("csv_files/Test.csv", '5', new_row)
# my_file_handler.get_rows_matching_search_criteria("csv_files/Test.csv", 'and', first='Jim', last='Alex')

# VEHICLE
# alex_car = Vehicle("csv_files/Vehicles.csv")
# # print(alex_car.get_car_by_features('and', owner='Ghidon ITC', color='yellow'))
# print(alex_car.get_time_to_test('4'))

# LOGGER
# log = Logger("logs", "log_file.txt")
# log.add_to_log("My new log message")

# CARLOT
my_car_lot = CarLot()
my_car_lot.employees_with_cars()
# # my_car_lot.update_salary_by_name("csv_files/User.csv", "Alex Bloom", 8000)
# vehicle_to_add = {'owner': 'Ruthy Lewis','brand': 'Toyota','color': 'Yellow','door_count': 4,'last_test': '5-07-1992'}
# # my_car_lot.add_to_fleet(vehicle_to_add)
# # my_car_lot.get_fleet_size()
# print(my_car_lot.get_fleet_size_by_brand("toyota"))




