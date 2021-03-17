from src.config import results_folder_name
from os import listdir
from os.path import isfile, join
import csv


class LearningAlgorithm ():
    """The Learning Algorithm is responsible for analysing the User's quiz results.

    Atrributes:
        results_path        (String)    Path to where quiz reuslts stored
        files_to_examine    (List)      List of quiz result files
        results_as_list     (List)
        results_map         (Dict)      Map of characters and information about them i.e. total attemts, correct answers etc
        sucess_rates        (List)      Sorted list of unique chars and thier success rates
    """

    results_path = results_folder_name
    files_to_examine = []
    results_map = {}
    results_as_list = []
    sucess_rates = []

    def __init__(self):
        """Initialises the object."""
        self.get_all_file_names()
        self.results_path = results_folder_name
        self.files_to_examine = []
        self.results_map = {}
        self.results_as_list = []
        self.sucess_rates = []

    def print_result_map(self):
        """Prints the results map."""
        for key, Value in self.results_map.items():
            print(f"{key} : {Value}")

    def get_all_file_names(self):
        """Gets all results files. Sets the objects value"""
        folder_path = self.results_path
        self.files_to_examine = [f for f in listdir(
            folder_path) if isfile(join(folder_path, f))]

    def get_results_map(self):
        """Returns results_map attribute"""
        return self.results_map

    def update_results_map(self, char, result):
        """Updates the results map.

        Parameters:
            char      (String)  Character to be updated.
            result    (String)  Result i.e +1 right, -1 Wrong
            """
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
        """Fetches the results from the files."""
        for file_name in list(self.files_to_examine):
            current_log_file_path = "{}/{}".format(
                self.results_path, file_name)
            print(current_log_file_path)

            with open(current_log_file_path, newline='') as csvfile:
                spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in spamreader:
                    self.results_as_list.append(row[0])

    def analyse_results(self):
        """Analyses the fetched results."""
        print("Results to process: {}".format(self.get_results_as_list()))
        for index, row in enumerate(self.results_as_list, start=1):
            if index > 1:
                current_row = row.split(",")
                char = current_row[2]
                result = current_row[3]
                print("CHAR: {} - RESULT: {}".format(char, result))
                self.update_results_map(char=char, result=result)

    def set_results_as_list(self, val):
        """Sets results_as_list"""
        self.results_as_list = val

    def get_results_as_list(self):
        """Gets results_as_list"""
        return self.results_as_list

    def calculate_success_rate(self):
        """Calculates the success rate of each char. Not ordered."""
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
        """Orders the list of success rates."""
        s = sorted(self.sucess_rates, key=lambda k: -k['success'])
        self.set_sucess_rates(s)

    def get_sucess_rates(self):
        """Gets results_as_list"""
        return self.sucess_rates

    def set_sucess_rates(self, val):
        """Sets results_as_list"""
        self.sucess_rates = val
