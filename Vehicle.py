from FileHandler import FileHandler


class Vehicle:
    vehicles_db = FileHandler()

    def __init__(self, path_to_vehicles_db):
        self.path_to_vehicles_db = path_to_vehicles_db

    def update_vehicle_with_id(self, id, **kwargs):
        return self.vehicles_db.update_csv(self.path_to_vehicles_db, id, kwargs)

    def get_car_by_features(self, and_or='and', **kwargs):
        return self.vehicles_db.get_rows_matching_search_criteria(self.path_to_vehicles_db, kwargs, and_or)
