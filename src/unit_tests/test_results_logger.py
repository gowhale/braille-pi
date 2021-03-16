import pytest
from src.results_logging.results_logger import ResultsLogger


# To run this file execute the following:
# pytest --cov-report term-missing --cov=error_reporting .

def test_results_logger():
    results_logger = ResultsLogger()
    results_logger.log_results(wrong_answers=[], correct_answers=[])
