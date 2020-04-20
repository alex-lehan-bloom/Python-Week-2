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
                    print(
                        "Error: A key in your 'data_to_add_to_csv' dictionary doesn't exist in the '{}' database".format(
                            file_name))
                csv_file.close()
                return True

    def remove_from_csv(self, file_name, test_id):
        file_contents = self.load_from_csv(file_name)
        new_file_contents = []
        id_exists = False
        for line in file_contents:
            print(line['user_id'])
            if line['user_id'] != test_id and id_exists == False:
                new_file_contents.append(line)
            elif line['user_id'] == test_id:
                id_exists = True
            else:
                line['user_id'] = int(line['user_id']) - 1
                new_file_contents.append(line)
        if id_exists == True:
            headers = self.get_csv_headers(file_name)
            try:
                csv_file = open(file_name, "w", newline='')
            except FileNotFoundError:
                print("Error: File not found: '{}'.".format(file_name))
            except IOError:
                print("Error: Could not open file: '{}'.".format(file_name))
            except Exception as e:
                print(e)
                print("Error: An unknown error occurred.")
            else:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(headers)
                csv_writer = csv.DictWriter(csv_file, fieldnames=headers)
                for line in new_file_contents:
                    csv_writer.writerow(line)
                return True
        else:
            return False

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
            headers = self.get_csv_headers(file_name)
            return headers

    def get_csv_headers(self, file_name):
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
            headers = next(file_contents).keys()
            csv_file.close()
            return headers


new_row = {'first': "Alex", 'last': "Alex", 'password': "Test", 'position': "Sad", 'salary': 10000, 'role': "SAeA"}
my_file_handler = FileHandler()
field_names = my_file_handler.get_csv_headers("csv_files/Test.csv")
print(my_file_handler.remove_from_csv("csv_files/Test.csv", '2'))
