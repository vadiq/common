import builtins

import mock
import pytest

from tests_practice.definitions import (
    task11,
    task12,
    task13,
    task14,
    task15,
    task16,
    task17,
    task18,
    task19,
    task20)


@pytest.mark.parametrize("a, b",
                         [(63, '1:3'), (48, '0:48'), (140, '2:20')])
def test_task11(a, b):
    assert task11(a) == b


def test_task11_raises():
    with pytest.raises(ValueError):
        task11(-5)


@pytest.mark.parametrize("a, b",
                         [("fun&!! &!!&!!54 times time", 'times'),
                          ("I love dogs", 'love'),
                          ('', None)])
def test_task12(a, b):
    assert task12(a) == b


def test_task12_raises():
    with pytest.raises(ValueError):
        task12(59)


@pytest.mark.parametrize("a, b",
                         [("My name is Michele", 'Michele is name My'),
                          ("I love dogs", 'dogs love I'),
                          ('', None)])
def test_task13(a, b):
    assert task13(a) == b


def test_task13_raises():
    with pytest.raises(ValueError):
        task13(59)


@pytest.mark.parametrize("a, b",
                         [(7, [1, 1, 2, 3, 5, 8, 13]),
                          (10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
                          (2, [1, 1]),
                          (1, [1])])
def test_task14(a, b):
    with mock.patch.object(builtins, 'input', lambda _: a):  # hereafter ".object" is unresolved reference,
        assert task14() == b                                 # but I can't mock input another way


def test_task14_raises():
    with mock.patch.object(builtins, 'input', lambda _: 'a'):
        with pytest.raises(ValueError):
            task14()


@pytest.mark.parametrize("a, b",
                         [([1, 4, 9, 16, 25, 36, 49, 64, 81, 100], [4, 16, 36, 64, 100]),
                          ([1, 9, 25], 'No even numbers')])
def test_task15(a, b):
    assert task15(a) == b


@pytest.mark.parametrize("a",
                         [59, []])
def test_task15_raises(a):
    with pytest.raises(ValueError):
        task15(a)


@pytest.mark.parametrize("a, b",
                         [(4, 10),
                          (2, 3)])
def test_task16(a, b):
    with mock.patch.object(builtins, 'input', lambda _: a):
        assert task16() == b


def test_task16_raises():
    with mock.patch.object(builtins, 'input', lambda _: 'a'):
        with pytest.raises(ValueError):
            task16()


@pytest.mark.parametrize("a, b",
                         [(4, 24),
                          (3, 6)])
def test_task17(a, b):
    assert task17(a) == b


@pytest.mark.parametrize("a",
                         ['59', [], 's'])
def test_task17_raises(a):
    with pytest.raises(ValueError):
        task17(a)


@pytest.mark.parametrize("a, b",
                         [('abcd', 'bcdE'),
                          ('efghi', 'fghIj')])
def test_task18(a, b):
    assert task18(a) == b


@pytest.mark.parametrize("a",
                         [59, []])
def test_task18_raises(a):
    with pytest.raises(ValueError):
        task18(a)


@pytest.mark.parametrize("a, b",
                         [('hello', 'ehllo'),
                          ('adbec', 'abcde')])
def test_task19(a, b):
    assert task19(a) == b


@pytest.mark.parametrize("a",
                         [59, []])
def test_task19_raises(a):
    with pytest.raises(ValueError):
        task19(a)


def test_task20():
    assert task20(5, 6)
    assert not task20(6, 5)
    assert task20(5, 5) == '-1'


@pytest.mark.parametrize("a, b",
                         [(59, '6'),
                          (5, [])])
def test_task20_raises(a, b):
    with pytest.raises(ValueError):
        task20(a, b)
