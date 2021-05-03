from src.config import results_folder_name
from os import listdir
from os.path import isfile, join
import csv
import random
import numpy as np


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
        for key, value in self.results_map.items():
            print(f"{key} : {value}")

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
            if result == "+1":
                self.results_map[char]["right"] += 1
                self.results_map[char]["total"] += 1
            elif result == "-1":
                self.results_map[char]["wrong"] += 1
                self.results_map[char]["total"] += 1

    def fetch_results(self):
        """Fetches the results from the files."""
        for file_name in list(self.files_to_examine):
            current_log_file_path = "{}/{}".format(
                self.results_path, file_name)

            with open(current_log_file_path, newline='') as csvfile:
                csv_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
                for row in csv_reader:
                    self.results_as_list.append(row[0])

    def analyse_results(self):
        """Analyses the fetched results."""
        for index, row in enumerate(self.results_as_list, start=1):
            if index > 1:
                current_row = row.split(",")
                char = current_row[2]
                result = current_row[3]
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

            success_rate = (count_correct/count_attempts)
            revision_weighting = 0.1+(1-(success_rate))
            char_success_rate = {"char": key, "success": (
                success_rate), "weight": revision_weighting}

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

    def get_worst_n_chars_elements(self, amount_of_characters):

        current_success_rates = self.get_sucess_rates()

        if amount_of_characters > len(current_success_rates):
            return current_success_rates
        else:
            return current_success_rates[-amount_of_characters:]

    def get_worst_n_characters(self, amount_of_characters):
        end_of_list = self.get_worst_n_chars_elements(amount_of_characters)
        characters_only = []
        for element in end_of_list:
            characters_only.append(element["char"])
        random.shuffle(characters_only)
        return characters_only

    def get_weighted_n_characters(self, amount_of_characters):

        all_success_rates = self.get_sucess_rates()

        if len(all_success_rates) > 0:

            elements = []
            weights = []
            for element in all_success_rates:

                char = element["char"]
                success_rate = element["weight"]
                elements.append(char)
                weights.append(success_rate)

            weight_sum = sum(weights)
            probabilities = []

            for weight in weights:
                probabilities.append(weight/weight_sum)

            if amount_of_characters > len(elements):
                amount_of_characters = len(elements)

            for char, probability in zip(elements, probabilities):
                probability_percentage = "{}%".format(
                    round(probability * 100, 2))
                print(
                    "Character: {:10} -> Probability it's selected: {:10}".format(char, probability_percentage))

            choice = np.random.choice(
                elements, size=amount_of_characters, replace=False, p=probabilities)

            characters_only = []
            for element in choice:
                characters_only.append(element)
            random.shuffle(characters_only)
            return characters_only

        else:
            return []

    def process_results(self):
        self.get_all_file_names()
        self.fetch_results()
        self.analyse_results()
        self.calculate_success_rate()
