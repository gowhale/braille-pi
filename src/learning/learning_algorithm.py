from src.config import results_folder_name
from os import listdir
from os.path import isfile, join
import csv


class LearningAlgorithm ():

    results_path = results_folder_name
    files_to_examine = []
    results_map = {}
    results_as_list = []
    sucess_rates = []

    def __init__(self):
        print("Learning Algorithm Initiated...")
        self.get_all_file_names()
        self.results_path = results_folder_name
        self.files_to_examine = []
        self.results_map = {}
        self.results_as_list = []
        self.sucess_rates = []

    def print_result_map(self):
        for key, Value in self.results_map.items():
            print(f"{key} : {Value}")

    def get_all_file_names(self):
        folder_path = self.results_path
        self.files_to_examine = [f for f in listdir(
            folder_path) if isfile(join(folder_path, f))]

    def get_results_map(self):
        return self.results_map

    def update_results_map(self, char, result):
        if char not in self.results_map:
            if result == "+1":
                self.results_map[char] = {
                    "wrong": 0,
                    "right": 1,
                    "total": 1,
                }
            elif result == "-1":
                self.results_map[char] = {
                    "wrong": 1,
                    "right": 0,
                    "total": 1,
                }
            else:
                print("Testing...")
        else:
            if result == "+1":
                self.results_map[char]["right"] += 1
                self.results_map[char]["total"] += 1
            elif result == "-1":
                self.results_map[char]["wrong"] += 1
                self.results_map[char]["total"] += 1
            else:
                print("Testing...")

        self.print_result_map()

    def fetch_results(self):

        for file_name in list(self.files_to_examine):
            current_log_file_path = "{}/{}".format(
                self.results_path, file_name)
            print(current_log_file_path)

            with open(current_log_file_path, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                    self.results_as_list.append(row[0])

    def analyse_results(self):
        print("Results to process: {}".format(self.get_results_as_list()))
        for index, row in enumerate(self.results_as_list, start=1):
            if index > 1:
                current_row = row.split(",")
                char = current_row[2]
                result = current_row[3]
                print("CHAR: {} - RESULT: {}".format(char, result))
                self.update_results_map(char=char, result=result)

    def set_results_as_list(self, val):
        self.results_as_list = val

    def get_results_as_list(self):
        return self.results_as_list

    def calculate_success_rate(self):
        for key in self.results_map:

            count_correct = self.results_map[key]["right"]
            count_attempts = self.results_map[key]["total"]

            print("Right: {}".format(count_correct))
            print("Total: {}".format(count_attempts))

            char_success_rate = {"char": key, "success": (
                count_correct/count_attempts)}

            self.sucess_rates.append(char_success_rate)

            self.sort_success_rates()

    def sort_success_rates(self):
        s = sorted(self.sucess_rates, key=lambda k: -k['success'])
        self.set_sucess_rates(s)

    def get_sucess_rates(self):
        return self.sucess_rates

    def set_sucess_rates(self, val):
        self.sucess_rates = val
