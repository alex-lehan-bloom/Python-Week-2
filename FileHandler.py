import csv


class FileHandler:
    def load_from_csv(self, file_name):
        try:
            csv_file = open(file_name, "r", newline='')
        except FileNotFoundError:
            print("Error: File not found: '{}'.".format(file_name))
        except IOError:
            print("Error: Could not read file: '{}'.".format(file_name))
        except Exception as e:
            print(e)
            print("Error: An unknown error occurred.")
        else:
            file_contents = csv.DictReader(csv_file)
            csv_file.close()
            return file_contents

    def append_to_csv(self, file_name, field_names, data_to_add_to_csv):
        try:
            csv_file = open(file_name, "a+", newline='')
        except FileNotFoundError:
            print("Error: File not found: '{}'.".format(file_name))
        except IOError:
            print("Error: Could not open file: '{}'.".format(file_name))
        except Exception as e:
            print(e)
            print("Error: An unknown error occurred.")
        else:
            csv_writer = csv.DictWriter(csv_file, fieldnames=field_names)
            user_id = self.get_num_rows(file_name) + 1
            try:
                data_to_add_to_csv['user_id'] = user_id
            except Exception as e:
                print("Error: You need to enter a dictionary for the 'data_to_add_to_csv' argument.")
            else:
                try:
                    csv_writer.writerow(data_to_add_to_csv)
                except ValueError as e:
                    print("Error: A key in your 'data_to_add_to_csv' dictionary doesn't exist in the '{}' database".format(file_name))
                csv_file.close()
                return True


    def get_num_rows(self, file_name):
        try:
            csv_file = open(file_name, "r", newline='')
        except FileNotFoundError:
            print("Error: File not found: '{}'.".format(file_name))
        except IOError:
            print("Error: Could not read file: '{}'.".format(file_name))
        except Exception as e:
            print(e)
            print("Error: An unknown error occurred.")
        else:
            file_contents = csv.DictReader(csv_file)
            return len(list(file_contents))


    def get_field_names_for_csv_file(self, file_name):
        try:
            csv_file = open(file_name, "r", newline='')
        except FileNotFoundError:
            print("Error: File not found: '{}'.".format(file_name))
        except IOError:
            print("Error: Could not read file: '{}'.".format(file_name))
        except Exception as e:
            print(e)
            print("Error: An unknown error occurred.")
        else:
            file_contents = csv.DictReader(csv_file)
            field_names = next(file_contents).keys()
            csv_file.close()
            return field_names


new_row = {'first':"Alex", 'last':"Alex", 'password':"Test", 'position': "Sad", 'salary': 10000, 'role': "SAeA"}
my_file_handler = FileHandler()
# my_file_handler.get_num_rows("csv_files/User.csv")
field_names = my_file_handler.get_field_names_for_csv_file("csv_files/User.csv")
my_file_handler.append_to_csv("csv_files/User.csv", field_names, new_row)
