from FileHandler import FileHandler
from Logger import Logger
from Vehicle import Vehicle
from CarLot import CarLot

# FILEHANDLER
# new_row = {'first': "New_first_name", 'last': "new_last_name"}
# my_file_handler = FileHandler()
# # field_names = get_csv_headers("csv_files/Test.csv")
# # # print(my_file_handler.remove_from_csv("csv_files/Test.csv", '2'))
# # my_file_handler.update_csv("csv_files/Test.csv", '5', new_row)
# my_file_handler.get_rows_matching_search_criteria("csv_files/Test.csv", 'and', first='Jim', last='Alex')

# VEHICLE
alex_car = Vehicle("csv_files/Vehicles.csv")
print(alex_car.get_car_by_features('and', owner='Ghidon ITC', color='yellow'))
