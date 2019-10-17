from unittest.mock import patch

import pytest

from tests_practice.definitions import (
    task11_time_converter,
    task12_largest_word,
    task13_words_backward,
    task14_fibonacci,
    task15_even_only,
    task16_sum_up_until,
    task17_factorial,
    task18_letter_replacement,
    task19_alpha_order,
    task20_num2_check)


@pytest.mark.parametrize("check, result",
                         [(63, '1:3'), (48, '0:48'), (140, '2:20')])
def test_task11_time_converter(check, result):
    assert task11_time_converter(check) == result


def test_task11_time_converter_raises():
    with pytest.raises(ValueError):
        task11_time_converter(-5)


@pytest.mark.parametrize("check, result",
                         [("fun&!! &!!&!!54 times time", 'times'),
                          ("I love dogs", 'love')])
def test_task12_largest_word(check, result):
    assert task12_largest_word(check) == result


def test_task12_largest_word_raises():
    with pytest.raises(ValueError):
        task12_largest_word(59)


@pytest.mark.parametrize("check, result",
                         [("My name is Michele", 'Michele is name My'),
                          ("I love dogs", 'dogs love I')])
def test_task13_words_backward(check, result):
    assert task13_words_backward(check) == result


def test_task13_words_backward_raises():
    with pytest.raises(ValueError):
        task13_words_backward(59)


@pytest.mark.parametrize("give_input, result",
                         [(7, [1, 1, 2, 3, 5, 8, 13]),
                          (10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
                          (2, [1, 1]),
                          (1, [1])])
def test_task14_fibonacci(give_input, result):
    with patch('builtins.input', return_value=give_input):
        assert task14_fibonacci() == result


def test_task14_fibonacci_raises():
    with patch('builtins.input', return_value='give_input'):
        with pytest.raises(ValueError):
            task14_fibonacci()


@pytest.mark.parametrize("check, result",
                         [([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], [4, 16, 36, 64, 100]),
                          ([1, 9, 25], [])])
def test_task15_even_only(check, result):
    assert task15_even_only(check) == result


@pytest.mark.parametrize("check",
                         [59, []])
def test_task15_even_only_raises(check):
    with pytest.raises(ValueError):
        task15_even_only(check)


@pytest.mark.parametrize("give_input, result",
                         [(4, 10),
                          (2, 3)])
def test_task16_sum_up_until(give_input, result):
    with patch('builtins.input', return_value=give_input):
        assert task16_sum_up_until() == result


def test_task16_sum_up_until_raises():
    with patch('builtins.input', return_value='give_input'):
        with pytest.raises(ValueError):
            task16_sum_up_until()


@pytest.mark.parametrize("check, result",
                         [(4, 24),
                          (3, 6)])
def test_task17_factorial(check, result):
    assert task17_factorial(check) == result


@pytest.mark.parametrize("check",
                         ['59', [], 's'])
def test_task17_factorial_raises(check):
    with pytest.raises(ValueError):
        task17_factorial(check)


@pytest.mark.parametrize("check, result",
                         [('abcd', 'bcdE'),
                          ('efghi', 'fghIj')])
def test_task18_letter_replacement(check, result):
    assert task18_letter_replacement(check) == result


@pytest.mark.parametrize("check",
                         [59, []])
def test_task18_letter_replacement_raises(check):
    with pytest.raises(ValueError):
        task18_letter_replacement(check)


@pytest.mark.parametrize("check, result",
                         [('hello', 'ehllo'),
                          ('adbec', 'abcde')])
def test_task19_alpha_order(check, result):
    assert task19_alpha_order(check) == result


@pytest.mark.parametrize("check",
                         [59, []])
def test_task19_alpha_order_raises(check):
    with pytest.raises(ValueError):
        task19_alpha_order(check)


def test_task20_num2_check():
    assert task20_num2_check(5, 6)
    assert not task20_num2_check(6, 5)
    assert task20_num2_check(5, 5) == '-1'


@pytest.mark.parametrize("check, result",
                         [(59, '6'),
                          (5, [])])
def test_task20_num2_check_raises(check, result):
    with pytest.raises(ValueError):
        task20_num2_check(check, result)
