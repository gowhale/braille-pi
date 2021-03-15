# Program Name: error_logger.py
# Description: This program will be used to log errros in a CSV file, it also generates a folder for the errors


import os
import csv
import datetime
from datetime import datetime


class ErrorLogger():

    """The purpose of this class is to make a folder to store error messages in.

    Attributes:
        error_log_directory     (String)    Address of the log directory.
        error_folder_name       (String)    Name of the error logs folder.
        now                     (DateTime)  Current DateTime object.
        date                    (String)    Just the date of the current DateTime object
        error_file_name         (String)    Formatted name of the file.
        log_file_path           (String)    Full path to where the file should be saved.
    """

    error_log_directory = ""
    error_folder_name = 'error_logs'
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    error_file_name = "{}-ERROR-LOG.csv".format(date)
    log_file_path = "{}/{}".format(error_folder_name, error_file_name)

    def __init__(self):
        """Creates a folder for error logs if not already created."""

        print("Creating a folder here: {}".format(self.error_log_directory))
        if not os.path.exists(self.error_folder_name):
            os.makedirs(self.error_folder_name)
            print("ERROR LOG CREATED")
        else:
            print("ERROR LOG ALREADY EXISTS")

        try:
            f = open(self.log_file_path)
            print("File exists")
            f.close()
        except IOError:
            print("Creating new file")

            with open(self.log_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["date", "time", "error"])

            file.close()

    def log_error(self, error):
        """Logs an error message to the error file.

        Parameters:
            error   (String)    Description of what error happened.
        """

        now = datetime.now()
        date = now.strftime("%d/%m/%Y")
        time = now.strftime("%H:%M:%S")
        fields = [date, time, error]
        with open(self.log_file_path, 'a') as f:
            writer = csv.writer(f)
            writer.writerow(fields)
        f.close()
