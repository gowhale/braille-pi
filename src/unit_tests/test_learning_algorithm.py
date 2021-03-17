from src.learning.learning_algorithm import LearningAlgorithm


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

    expected_output = [{"char": "a", "success": 0.5}]

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

    expected_output = [{"char": "a", "success": 0.5}]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_worst_n_chars_elements(amount_of_characters=1) == expected_output


def test_learning_algorithm_get_worst_n_chars_one_char_request_too_big():

    mocked_logged_results = """date,time,character,result
16/03/2021,14:01:21,a,+1
16/03/2021,14:01:21,a,-1""".split("\n")

    expected_output = [{"char": "a", "success": 0.5}]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_worst_n_chars_elements(amount_of_characters=5) == expected_output


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

    expected_output = [{"char": "g", "success": 1},
                       {"char": "a", "success": 0.0}]

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

    expected_output = [{"char": "a", "success": 1},
                       {"char": "z", "success": 1},
                       {"char": "b", "success": 0.5},
                       {"char": "d", "success": 0.25}, ]

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

    expected_output = [{"char": "a", "success": 1},
                       {"char": "z", "success": 1},
                       {"char": "b", "success": 0.5},
                       {"char": "d", "success": 0.25}, ]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_worst_n_chars_elements(amount_of_characters=5) == expected_output


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

    expected_output = [{"char": "b", "success": 0.5},
                       {"char": "d", "success": 0.25}, ]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_worst_n_chars_elements(amount_of_characters=2) == expected_output


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
        {"char": "d", "success": 0.25}, ]

    print(mocked_logged_results)

    a = LearningAlgorithm()
    a.set_results_as_list(mocked_logged_results)

    a.analyse_results()
    a.print_result_map()
    a.calculate_success_rate()

    assert a.get_worst_n_chars_elements(amount_of_characters=1) == expected_output


def test_learning_algorithm_default():
    learning_algorithm = LearningAlgorithm()
    learning_algorithm.fetch_results()
    learning_algorithm.analyse_results()
    learning_algorithm.print_result_map()
