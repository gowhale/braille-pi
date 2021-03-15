import pytest
from src.interaction.keyboard_interface import inverse_value, check_keys
import pygame


def test_keyboard_interface_inverse_value_1():
    test_input = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    test_expected_output = {
        1: 0,
        2: 0,
        3: 1,
        4: 0,
        5: 0,
        6: 0,
    }

    assert inverse_value(test_input, 3) == test_expected_output


def test_keyboard_interface_inverse_value_2():
    test_input = {
        1: 0,
        2: 0,
        3: 1,
        4: 0,
        5: 0,
        6: 0,
    }

    test_expected_output = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0,
        6: 0,
    }

    assert inverse_value(test_input, 3) == test_expected_output


def test_keys_pressed():
    key_presses = {
        "F": 0,
        "D": 0,
        "S": 0,
        "J": 0,
        "K": 0,
        "L": 0
    }

    check_keys(pygame, key_presses)
