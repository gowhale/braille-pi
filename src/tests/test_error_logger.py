import pytest
from src.error_reporting.error_logger import ErrorLogger


# To run this file execute the following:
# pytest --cov-report term-missing --cov=error_reporting .

def test_log_error():
    error_logger = ErrorLogger()
    error_logger.log_error("TESTING")


def test_translation_key_error():
    error_logger = ErrorLogger()
    # error_logger.error_log_directory =
    error_logger.log_error("TESTING")
