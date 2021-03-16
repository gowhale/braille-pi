from src.learning.learning_algorithm import LearningAlgorithm


def test_learning_algorithm_default():
    learning_algorithm = LearningAlgorithm()
    learning_algorithm.fetch_results()
    learning_algorithm.analyse_results()
    learning_algorithm.print_result_map()


def test_learning_algorithm_mocked():

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

    learning_algorithm = LearningAlgorithm()
    learning_algorithm.set_results_as_list(mocked_logged_results)

    learning_algorithm.analyse_results()
    learning_algorithm.print_result_map()

    assert learning_algorithm.get_results_map() == expected_output
