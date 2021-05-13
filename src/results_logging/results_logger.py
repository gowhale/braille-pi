# Program Name: results_logger.py
# Description: This program will be used to log errros in a CSV file, it also generates a folder for the quiz results


import os
import csv
import datetime
from datetime import datetime
from src.config import results_folder_name


class ResultsLogger():

    """The purpose of this class is to make a folder to store results from character attempts.

    Attributes:
        results_log_directory   (String)    Address of the log directory.
        results_folder_name     (String)    Name of the results logs folder.
        now                     (DateTime)  Current DateTime object.
        date                    (String)    Just the date of the current DateTime object
        results_file_name       (String)    Formatted name of the file.
        log_file_path           (String)    Full path to where the file should be saved.
    """

    results_log_directory = ""
    results_folder_name = results_folder_name
    now = datetime.now()
    date = now.strftime("%d-%m-%Y")
    results_file_name = "{}-QUIZ-RESULTS.csv".format(date)
    log_file_path = "{}/{}".format(results_folder_name, results_file_name)

    def __init__(self):
        """Creates a folder for results logs if not already created."""

        print("Creating a folder here: {}".format(self.results_log_directory))
        if not os.path.exists(self.results_folder_name):
            os.makedirs(self.results_folder_name)
            print("QUIZ LOG CREATED")
        else:
            print("QUIZ LOG ALREADY EXISTS")

        try:
            f = open(self.log_file_path)
            print("File exists")
            f.close()
        except IOError:
            print("Creating new file")

            with open(self.log_file_path, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["date", "time", "character", "result"])

            file.close()

    def log_results(self, correct_answers, wrong_answers):
        """Logs quiz results message to the quiz file.

        Parameters:
            results   (String)    Description of what results happened.
        """

        with open(self.log_file_path, 'a') as f:
            for answer in correct_answers:
                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")
                fields = [date, time, answer, "+1"]
                writer = csv.writer(f)
                writer.writerow(fields)
            f.close()

        with open(self.log_file_path, 'a') as f:
            for answer in wrong_answers:
                now = datetime.now()
                date = now.strftime("%d/%m/%Y")
                time = now.strftime("%H:%M:%S")
                fields = [date, time, answer, "-1"]
                writer = csv.writer(f)
                writer.writerow(fields)
            f.close()
