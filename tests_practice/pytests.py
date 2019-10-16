import builtins

import mock
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


@pytest.mark.parametrize("a, b",
                         [(63, '1:3'), (48, '0:48'), (140, '2:20')])
def test_task11_time_converter(a, b):
    assert task11_time_converter(a) == b


def test_task11_time_converter_raises():
    with pytest.raises(ValueError):
        task11_time_converter(-5)


@pytest.mark.parametrize("a, b",
                         [("fun&!! &!!&!!54 times time", 'times'),
                          ("I love dogs", 'love'),
                          ('', None)])
def test_task12_largest_word(a, b):
    assert task12_largest_word(a) == b


def test_task12_largest_word_raises():
    with pytest.raises(ValueError):
        task12_largest_word(59)


@pytest.mark.parametrize("a, b",
                         [("My name is Michele", 'Michele is name My'),
                          ("I love dogs", 'dogs love I'),
                          ('', None)])
def test_task13_words_backward(a, b):
    assert task13_words_backward(a) == b


def test_task13_words_backward_raises():
    with pytest.raises(ValueError):
        task13_words_backward(59)


@pytest.mark.parametrize("a, b",
                         [(7, [1, 1, 2, 3, 5, 8, 13]),
                          (10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
                          (2, [1, 1]),
                          (1, [1])])
def test_task14_fibonacci(a, b):
    with mock.patch.object(builtins, 'input', lambda _: a):  # hereafter ".object" is unresolved reference,
        assert task14_fibonacci() == b                                 # but I can't mock input another way


def test_task14_fibonacci_raises():
    with mock.patch.object(builtins, 'input', lambda _: 'a'):
        with pytest.raises(ValueError):
            task14_fibonacci()


@pytest.mark.parametrize("a, b",
                         [([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], [4, 16, 36, 64, 100]),
                          ([1, 9, 25], 'No even numbers')])
def test_task15_even_only(a, b):
    assert task15_even_only(a) == b


@pytest.mark.parametrize("a",
                         [59, []])
def test_task15_even_only_raises(a):
    with pytest.raises(ValueError):
        task15_even_only(a)


@pytest.mark.parametrize("a, b",
                         [(4, 10),
                          (2, 3)])
def test_task16_sum_up_until(a, b):
    with mock.patch.object(builtins, 'input', lambda _: a):
        assert task16_sum_up_until() == b


def test_task16_sum_up_until_raises():
    with mock.patch.object(builtins, 'input', lambda _: 'a'):
        with pytest.raises(ValueError):
            task16_sum_up_until()


@pytest.mark.parametrize("a, b",
                         [(4, 24),
                          (3, 6)])
def test_task17_factorial(a, b):
    assert task17_factorial(a) == b


@pytest.mark.parametrize("a",
                         ['59', [], 's'])
def test_task17_factorial_raises(a):
    with pytest.raises(ValueError):
        task17_factorial(a)


@pytest.mark.parametrize("a, b",
                         [('abcd', 'bcdE'),
                          ('efghi', 'fghIj')])
def test_task18_letter_replacement(a, b):
    assert task18_letter_replacement(a) == b


@pytest.mark.parametrize("a",
                         [59, []])
def test_task18_letter_replacement_raises(a):
    with pytest.raises(ValueError):
        task18_letter_replacement(a)


@pytest.mark.parametrize("a, b",
                         [('hello', 'ehllo'),
                          ('adbec', 'abcde')])
def test_task19_alpha_order(a, b):
    assert task19_alpha_order(a) == b


@pytest.mark.parametrize("a",
                         [59, []])
def test_task19_alpha_order_raises(a):
    with pytest.raises(ValueError):
        task19_alpha_order(a)


def test_task20_num2_check():
    assert task20_num2_check(5, 6)
    assert not task20_num2_check(6, 5)
    assert task20_num2_check(5, 5) == '-1'


@pytest.mark.parametrize("a, b",
                         [(59, '6'),
                          (5, [])])
def test_task20_num2_check_raises(a, b):
    with pytest.raises(ValueError):
        task20_num2_check(a, b)
