import csv
from collections import OrderedDict


def get_csv_headers(file_name):
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

    def append_to_csv(self, file_name, data_to_add_to_csv):
        try:
            csv_file = open(file_name, "a+", newline='')
        except FileNotFoundError:
            print("Error: File not found: '{}'.".format(file_name))
            return False
        except IOError:
            print("Error: Could not open file: '{}'.".format(file_name))
            return False
        except Exception as e:
            print(e)
            print("Error: An unknown error occurred.")
            return False
        else:
            csv_writer = csv.DictWriter(csv_file, fieldnames=get_csv_headers(file_name))
            id = self.get_num_rows(file_name) + 1
            try:
                data_to_add_to_csv['id'] = id
            except Exception as e:
                print("Error: You need to enter a dictionary for the 'data_to_add_to_csv' argument.")
            else:
                try:
                    csv_writer.writerow(data_to_add_to_csv)
                    return True
                except ValueError as e:
                    print(e)
                    print(
                        "Error: A key in your 'data_to_add_to_csv' dictionary doesn't exist in the '{}' database".format(
                            file_name))
                    return False

    def update_csv(self, file_name, id, updated_info):
        file_contents = self.load_from_csv(file_name)
        new_file_contents = []
        id_exists = False
        for line in file_contents:
            if line['id'] != id:
                new_file_contents.append(line)
            else:
                id_exists = True
                for key in updated_info:
                    line[key] = updated_info[key]
                line = OrderedDict(line.items())
                new_file_contents.append(line)
        headers = get_csv_headers(file_name)
        if id_exists == True:
            headers = get_csv_headers(file_name)
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
                    try:
                        csv_writer.writerow(line)
                    except Exception as e:
                        print(e)
                        print(
                            "Error: A key in your 'data_to_add_to_csv' dictionary doesn't exist in the '{}' database".format(
                                file_name))
                return True
        else:
            return False

    def remove_from_csv(self, file_name, id):
        file_contents = self.load_from_csv(file_name)
        new_file_contents = []
        id_exists = False
        for line in file_contents:
            print(line['id'])
            if line['id'] != id and id_exists == False:
                new_file_contents.append(line)
            elif line['id'] == id:
                id_exists = True
            else:
                line['id'] = int(line['id']) - 1
                new_file_contents.append(line)
        if id_exists == True:
            headers = get_csv_headers(file_name)
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
            return False
        except IOError:
            print("Error: Could not read file: '{}'.".format(file_name))
            return False
        except Exception as e:
            print(e)
            print("Error: An unknown error occurred.")
            return False
        else:
            file_contents = csv.DictReader(csv_file)
            return len(list(file_contents))

    def get_num_rows_matching_search_criteria(self, file_name, field, search_criteria):
        header_exists = False
        headers = get_csv_headers(file_name)
        for i in headers:
            if i == field:
                header_exists = True
        if not header_exists:
            print("The '{}' field doesn't exist in the '{}' file.".format(field, file_name))
            return False
        file_contents = self.load_from_csv(file_name)
        count = 0
        for line in file_contents:
            if line[field].lower() == search_criteria.lower():
                count += 1
        return count






new_row = {'first': "New_first_name", 'last': "new_last_name"}
my_file_handler = FileHandler()
# field_names = get_csv_headers("csv_files/Test.csv")
# # print(my_file_handler.remove_from_csv("csv_files/Test.csv", '2'))
my_file_handler.update_csv("csv_files/Test.csv", '5', new_row)
