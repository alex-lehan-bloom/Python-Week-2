import csv

class FileHandler:

    # Maybe need self as arg too?
    def load_from_csv(self, file_name):
        try:
            csv_file = open(file_name, "r", newline='')
        except FileNotFoundError:
            print("Error: File not found: '{}'.".format(file_name))
        except Exception as e:
            print(e)
            print("Error: An unknown error occurred.")
        else:
            reader = csv.DictReader(csv_file)
            for row in reader:
                print(row)

my_file_handler = FileHandler()
my_file_handler.load_from_csv("csv_files/User.csv")