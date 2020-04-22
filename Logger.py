from datetime import datetime
import os


def how_long_has_file_existed(log_file):
    time_file_created = log_file.split(".")[1]
    time_since_file_created = datetime.now() - datetime.strptime(time_file_created, "%d-%m-%Y-%H-%M-%S")
    time_since_file_created_hours = time_since_file_created.seconds / 3600
    return time_since_file_created_hours


class Logger:
    def __init__(self, path_to_log_file, log_file_name):
        self.dir_path = path_to_log_file
        self.name = log_file_name
        self.new_file_name = None

    def add_to_log(self, msg):
        self.__delete_files_older_than_24_hours()
        date = datetime.now()
        self.create_dir_path()
        f = self.open_log_file()
        try:
            f.write(date.strftime("%y/%m/%Y, %H:%M:%S") + " {} \n".format(msg))
        except Exception as e:
            print(e)
            print("Error: Could not write to file.")
        else:
            print("Successfully created new log entry at {}".format(self.new_file_name))
        f.close()

    def open_log_file(self):
        files_in_log_directory = self.list_dir_items()
        # If directory is empty, create a new file
        if not files_in_log_directory:
            self.new_file_name = self.generate_new_log_file_name()
        # If there is a log file, use the existng log file if it was created within the hour. Otherwise, create a new log file.
        else:
            newest_log_file = files_in_log_directory[-1]
            file_create_time = how_long_has_file_existed(newest_log_file)
            if file_create_time > 1:
                self.new_file_name = self.generate_new_log_file_name()
            else:
                self.new_file_name = "{}\\{}".format(self.dir_path, newest_log_file)
        try:
            f = open(self.new_file_name, "a+")
        except OSError as e:
            print("Error:", e.strerror)
        except Exception as e:
            print("Error: Unknown error occurred.")
        else:
            return f

    def create_dir_path(self):
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)

    def generate_new_log_file_name(self):
        date = datetime.now()
        new_name = self.name.split(".")
        new_name.insert(1, date.strftime("%d-%m-%Y-%H-%M-%S"))
        new_name = ".".join(new_name)
        file_path = "{}\\{}".format(self.dir_path, new_name)
        return file_path

    def list_dir_items(self):
        dir_items = os.listdir(self.dir_path)
        dir_items = sorted(dir_items, key=lambda date: datetime.strptime(date, "log_file.%y-%m-%Y-%H-%M-%S.txt"),reverse=False)
        return dir_items

    def __delete_files_older_than_24_hours(self):
        files_in_log_directory = self.list_dir_items()
        for file in files_in_log_directory:
            time_since_file_created = how_long_has_file_existed(file)
            if time_since_file_created > 24:
                os.remove("{}\\{}".format(self.dir_path, file))
