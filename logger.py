import datetime
import os

class Logger():
    def __init__(self, path_to_log_file, log_file_name):
        self.dir_path = path_to_log_file
        self.name = log_file_name
        self.full_path = "{}\\{}".format(self.dir_path, self.name)


    def create_log_entry(self, msg):
        if not os.path.exists(self.dir_path):
            os.makedirs(self.dir_path)
        try:
            f = open(self.full_path, "a+")
        except OSError as e:
            if e.strerror == "No such file or directory exists":
                f.close()
                f.open(self.full_path, "w")
            else:
                print("Error:", e.strerror)
        except Exception as e:
            print("Error: Unknown error occurred.")
        else:
            date = datetime.datetime.now()
            try:
                f.write(date.strftime("%y/%m/%Y, %H:%M:%S") + "{} \n".format(msg))
            except Exception as e:
                print(e)
                print("Error: Could not write to file.")
            else:
                print("Successfully created new log entry at {}".format(self.dir_path))
            f.close()

log = Logger("logs", "log_file.txt")
log.create_log_entry("A test message")

