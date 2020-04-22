from FileHandler import FileHandler


class Vehicle:
    vehicles_db = FileHandler()
    def __init__(self,path_to_vehicles_db):
        self.path_to_vehicles_db = path_to_vehicles_db


    def update_vehicle_with_id(self, id, **kwargs):
        test = self.vehicles_db.update_csv(self.path_to_vehicles_db, id, kwargs)
        print(test)


my_vehicle = Vehicle("csv_files/Vehicles.csv")
my_vehicle.update_vehicle_with_id('8', brand="New_brand", owner="Tim Palace")

