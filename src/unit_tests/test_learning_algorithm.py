# File Description: This unit test ensures that the Learning Algorithm is performing as expected

from src.learning.learning_algorithm import LearningAlgorithm
from statistics import mean

AMOUNT_OF_SIMULATIONS = 100


def test_learning_algorithm_results_map():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,b,+1
16/03/2021,14:01:21,c,+1
16/03/2021,14:01:21,d,+1
16/03/2021,14:01:21,e,+1
16/03/2021,14:01:21,f,+1
16/03/2021,14:01:21,g,+1
16/03/2021,14:01:21,h,+1
16/03/2021,14:01:21,i,+1
16/03/2021,14:01:21,j,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,b,+1
16/03/2021,14:01:21,c,+1
16/03/2021,14:01:21,d,+1
16/03/2021,14:01:21,e,+1
16/03/2021,14:01:21,f,+1
16/03/2021,14:01:21,g,+1
16/03/2021,14:01:21,h,+1
16/03/2021,14:01:21,i,+1
16/03/2021,14:01:21,j,+1""".split("\n")

    expected_output = {"a": {'wrong': 0, 'right': 2, 'total': 2},
                       "b": {'wrong': 0, 'right': 2, 'total': 2},
                       "c": {'wrong': 0, 'right': 2, 'total': 2},
                       "d": {'wrong': 0, 'right': 2, 'total': 2},
                       "e": {'wrong': 0, 'right': 2, 'total': 2},
                       "f": {'wrong': 0, 'right': 2, 'total': 2},
                       "g": {'wrong': 0, 'right': 2, 'total': 2},
                       "h": {'wrong': 0, 'right': 2, 'total': 2},
                       "i": {'wrong': 0, 'right': 2, 'total': 2},
                       "j": {'wrong': 0, 'right': 2, 'total': 2}}

    print(mocked_logged_results)

    l = LearningAlgorithm()
    l.set_results_as_list(mocked_logged_results)

    l.analyse_results()
    l.print_result_map()

    assert l.get_results_map() == expected_output


def test_learning_algorithm_success_rate_empty_file():

    mocked_logged_results = """""".split("\n")

    expected_output = []

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_sucess_rates() == expected_output


def test_learning_algorithm_success_rate_one_char():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,-1""".split("\n")

    expected_output = [{"char": "a", "success": 0.5, 'weight': 0.6}]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_sucess_rates() == expected_output


def test_learning_algorithm_get_worst_n_chars_one_char():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,-1""".split("\n")

    expected_output = [{"char": "a", "success": 0.5, 'weight': 0.6}]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_worst_n_chars_elements(
        amount_of_characters=1) == expected_output


def test_learning_algorithm_get_worst_n_chars_one_char_request_too_big():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,-1""".split("\n")

    expected_output = [{"char": "a", "success": 0.5, 'weight': 0.6}]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_worst_n_chars_elements(
        amount_of_characters=5) == expected_output


def test_learning_algorithm_success_edge_cases():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,-1
16/03/2021,14:01:21,a,-1
16/03/2021,14:01:21,a,-1
16/03/2021,14:01:21,a,-1
16/03/2021,14:01:21,a,-1
16/03/2021,14:01:21,a,-1
16/03/2021,14:01:21,a,-1
16/03/2021,14:01:21,g,+1
16/03/2021,14:01:21,a,-1""".split("\n")

    expected_output = [{"char": "g", "success": 1, 'weight': 0.1},
                       {"char": "a", "success": 0.0, 'weight': 1.1}]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_sucess_rates() == expected_output


def test_learning_algorithm_success_rate_multiple_chars():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,b,+1
16/03/2021,14:01:21,b,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,z,+1
16/03/2021,14:01:21,a,+1""".split("\n")

    expected_output = [{"char": "a", "success": 1, 'weight': 0.1},
                       {"char": "z", "success": 1, 'weight': 0.1},
                       {"char": "b", "success": 0.5, 'weight': 0.6},
                       {"char": "d", "success": 0.25, 'weight': 0.85}, ]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_sucess_rates() == expected_output


def test_learning_algorithm_get_worst_n_chars_multiple_chars():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,b,+1
16/03/2021,14:01:21,b,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,z,+1
16/03/2021,14:01:21,a,+1""".split("\n")

    expected_output = [{"char": "a", "success": 1, 'weight': 0.1},
                       {"char": "z", "success": 1, 'weight': 0.1},
                       {"char": "b", "success": 0.5, 'weight': 0.6},
                       {"char": "d", "success": 0.25, 'weight': 0.85}]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_worst_n_chars_elements(
        amount_of_characters=5) == expected_output


def test_learning_algorithm_get_worst_n_chars_multiple_chars_2_return():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,b,+1
16/03/2021,14:01:21,b,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,z,+1
16/03/2021,14:01:21,a,+1""".split("\n")

    expected_output = [{"char": "b", "success": 0.5, 'weight': 0.6},
                       {"char": "d", "success": 0.25, 'weight': 0.85}]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_worst_n_chars_elements(
        amount_of_characters=2) == expected_output


def test_learning_algorithm_get_worst_n_chars_multiple_chars_1_return():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,b,+1
16/03/2021,14:01:21,b,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,d,+1
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,z,+1
16/03/2021,14:01:21,a,+1""".split("\n")

    expected_output = [
        {"char": "d", "success": 0.25, 'weight': 0.85}, ]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_worst_n_chars_elements(
        amount_of_characters=1) == expected_output


def test_learning_algorithm_default():
    learning_algorithm = LearningAlgorithm()
    learning_algorithm.fetch_results()
    learning_algorithm.analyse_results()
    learning_algorithm.print_result_map()


def test_quiz_selection_when_weakness_is_vowels():
    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,-1
16/03/2021,14:01:21,b,+1
16/03/2021,14:01:21,c,+1
16/03/2021,14:01:21,d,+1
16/03/2021,14:01:21,e,-1
16/03/2021,14:01:21,f,+1
16/03/2021,14:01:21,g,+1
16/03/2021,14:01:21,h,+1
16/03/2021,14:01:21,i,-1
16/03/2021,14:01:21,j,+1
16/03/2021,14:01:21,k,+1
16/03/2021,14:01:21,l,+1
16/03/2021,14:01:21,m,+1
16/03/2021,14:01:21,n,+1
16/03/2021,14:01:21,o,-1
16/03/2021,14:01:21,p,+1
16/03/2021,14:01:21,q,+1
16/03/2021,14:01:21,r,+1
16/03/2021,14:01:21,s,+1
16/03/2021,14:01:21,t,+1
16/03/2021,14:01:21,u,-1
16/03/2021,14:01:21,v,+1
16/03/2021,14:01:21,w,+1
16/03/2021,14:01:21,x,+1
16/03/2021,14:01:21,y,+1
16/03/2021,14:01:21,z,+1""".split("\n")

    learning_algorithm = LearningAlgorithm()
    learning_algorithm.set_results_as_list(mocked_logged_results)

    learning_algorithm.analyse_results()
    learning_algorithm.print_result_map()
    learning_algorithm.calculate_success_rate()

    count_occurences = {}

    amount_of_tests = AMOUNT_OF_SIMULATIONS

    for _ in range(amount_of_tests):
        choices = learning_algorithm.get_weighted_n_characters(
            5)
        # print(choices)
        for char in choices:
            if char in count_occurences:
                count_occurences[char] += 1
            else:
                count_occurences[char] = 1

    vowels = list("aeiou")
    vowels_results = []
    consonant_results = []

    for char in count_occurences:
        percentage_in_quiz = round(
            count_occurences[char] / amount_of_tests * 100, 2)
        print("Char: {}, Count: {}".format(char, percentage_in_quiz))
        if char in vowels:
            vowels_results.append(percentage_in_quiz)
        else:
            consonant_results.append(percentage_in_quiz)

    vowels_average = mean(vowels_results)
    consonant_average = mean(consonant_results)

    print("Vowels average percentage in quiz: {}".format(vowels_average))
    print("Consonant average percentage in quiz: {}".format(consonant_average))

    assert vowels_average > consonant_average


def test_quiz_selection_when_weakness_is_consonants():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,b,-1
16/03/2021,14:01:21,c,-1
16/03/2021,14:01:21,d,-1
16/03/2021,14:01:21,e,+1
16/03/2021,14:01:21,f,-1
16/03/2021,14:01:21,g,-1
16/03/2021,14:01:21,h,-1
16/03/2021,14:01:21,i,+1
16/03/2021,14:01:21,j,-1
16/03/2021,14:01:21,k,-1
16/03/2021,14:01:21,l,-1
16/03/2021,14:01:21,m,-1
16/03/2021,14:01:21,n,-1
16/03/2021,14:01:21,o,+1
16/03/2021,14:01:21,p,-1
16/03/2021,14:01:21,q,-1
16/03/2021,14:01:21,r,-1
16/03/2021,14:01:21,s,-1
16/03/2021,14:01:21,t,-1
16/03/2021,14:01:21,u,+1
16/03/2021,14:01:21,v,-1
16/03/2021,14:01:21,w,-1
16/03/2021,14:01:21,x,-1
16/03/2021,14:01:21,y,-1
16/03/2021,14:01:21,z,-1""".split("\n")

    learning_algorithm = LearningAlgorithm()
    learning_algorithm.set_results_as_list(mocked_logged_results)

    learning_algorithm.analyse_results()
    learning_algorithm.print_result_map()
    learning_algorithm.calculate_success_rate()

    count_occurences = {}

    amount_of_tests = AMOUNT_OF_SIMULATIONS

    for _ in range(amount_of_tests):
        choices = learning_algorithm.get_weighted_n_characters(
            5)
        # print(choices)
        for char in choices:
            if char in count_occurences:
                count_occurences[char] += 1
            else:
                count_occurences[char] = 1

    vowels = list("aeiou")
    vowels_results = []
    consonant_results = []

    for char in count_occurences:
        percentage_in_quiz = round(
            count_occurences[char] / amount_of_tests * 100, 2)
        print("Char: {}, Count: {}".format(char, percentage_in_quiz))
        if char in vowels:
            vowels_results.append(percentage_in_quiz)
        else:
            consonant_results.append(percentage_in_quiz)

    vowels_average = mean(vowels_results)
    consonant_average = mean(consonant_results)

    print("Vowels average percentage in quiz: {}".format(vowels_average))
    print("Consonant average percentage in quiz: {}".format(consonant_average))

    assert vowels_average < consonant_average


def test_quiz_selection_when_weakness_is_vowels():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,-1
16/03/2021,14:01:21,b,+1
16/03/2021,14:01:21,c,+1
16/03/2021,14:01:21,d,+1
16/03/2021,14:01:21,e,-1
16/03/2021,14:01:21,f,+1
16/03/2021,14:01:21,g,+1
16/03/2021,14:01:21,h,+1
16/03/2021,14:01:21,i,-1
16/03/2021,14:01:21,j,+1
16/03/2021,14:01:21,k,+1
16/03/2021,14:01:21,l,+1
16/03/2021,14:01:21,m,+1
16/03/2021,14:01:21,n,+1
16/03/2021,14:01:21,o,-1
16/03/2021,14:01:21,p,+1
16/03/2021,14:01:21,q,+1
16/03/2021,14:01:21,r,+1
16/03/2021,14:01:21,s,+1
16/03/2021,14:01:21,t,+1
16/03/2021,14:01:21,u,-1
16/03/2021,14:01:21,v,+1
16/03/2021,14:01:21,w,+1
16/03/2021,14:01:21,x,+1
16/03/2021,14:01:21,y,+1
16/03/2021,14:01:21,z,+1""".split("\n")

    learning_algorithm = LearningAlgorithm()
    learning_algorithm.set_results_as_list(mocked_logged_results)

    learning_algorithm.analyse_results()
    learning_algorithm.print_result_map()
    learning_algorithm.calculate_success_rate()

    count_occurences = {}

    amount_of_tests = AMOUNT_OF_SIMULATIONS

    for _ in range(amount_of_tests):
        choices = learning_algorithm.get_weighted_n_characters(
            5)
        # print(choices)
        for char in choices:
            if char in count_occurences:
                count_occurences[char] += 1
            else:
                count_occurences[char] = 1

    vowels = list("aeiou")
    vowels_results = []
    consonant_results = []

    for char in count_occurences:
        percentage_in_quiz = round(
            count_occurences[char] / amount_of_tests * 100, 2)
        print("Char: {}, Count: {}".format(char, percentage_in_quiz))
        if char in vowels:
            vowels_results.append(percentage_in_quiz)
        else:
            consonant_results.append(percentage_in_quiz)

    vowels_average = mean(vowels_results)
    consonant_average = mean(consonant_results)

    print("Vowels average percentage in quiz: {}".format(vowels_average))
    print("Consonant average percentage in quiz: {}".format(consonant_average))

    assert vowels_average > consonant_average


def test_quiz_selection_when_weakness_is_letter_a():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,-1
16/03/2021,14:01:21,b,+1
16/03/2021,14:01:21,c,+1
16/03/2021,14:01:21,d,+1
16/03/2021,14:01:21,e,+1
16/03/2021,14:01:21,f,+1
16/03/2021,14:01:21,g,+1
16/03/2021,14:01:21,h,+1
16/03/2021,14:01:21,i,+1
16/03/2021,14:01:21,j,+1
16/03/2021,14:01:21,k,+1
16/03/2021,14:01:21,l,+1
16/03/2021,14:01:21,m,+1
16/03/2021,14:01:21,n,+1
16/03/2021,14:01:21,o,+1
16/03/2021,14:01:21,p,+1
16/03/2021,14:01:21,q,+1
16/03/2021,14:01:21,r,+1
16/03/2021,14:01:21,s,+1
16/03/2021,14:01:21,t,+1
16/03/2021,14:01:21,u,+1
16/03/2021,14:01:21,v,+1
16/03/2021,14:01:21,w,+1
16/03/2021,14:01:21,x,+1
16/03/2021,14:01:21,y,+1
16/03/2021,14:01:21,z,+1""".split("\n")

    learning_algorithm = LearningAlgorithm()
    learning_algorithm.set_results_as_list(mocked_logged_results)

    learning_algorithm.analyse_results()
    learning_algorithm.print_result_map()
    learning_algorithm.calculate_success_rate()

    count_occurences = {}

    amount_of_tests = AMOUNT_OF_SIMULATIONS

    for _ in range(amount_of_tests):
        choices = learning_algorithm.get_weighted_n_characters(
            5)
        # print(choices)
        for char in choices:
            if char in count_occurences:
                count_occurences[char] += 1
            else:
                count_occurences[char] = 1

    vowels = list("a")
    vowels_results = []
    consonant_results = []

    for char in count_occurences:
        percentage_in_quiz = round(
            count_occurences[char] / amount_of_tests * 100, 2)
        print("Char: {}, Count: {}".format(char, percentage_in_quiz))
        if char in vowels:
            vowels_results.append(percentage_in_quiz)
        else:
            consonant_results.append(percentage_in_quiz)

    weaker_characters = mean(vowels_results)
    stronger_characters = mean(consonant_results)

    print("Vowels average percentage in quiz: {}".format(weaker_characters))
    print("Consonant average percentage in quiz: {}".format(stronger_characters))

    assert weaker_characters > stronger_characters
