import unittest

from tests_practice.definitions import (
    task1_common_elements,
    task2_letter_times,
    task3_is_power,
    task4_add_repeatedly,
    task5_push_zeros,
    task6_arithmetic_progression_check,
    task7_unique_number,
    task8_missing_number,
    task9_find_before_tuple,
    task10_string_reversed
)


class TestCases(unittest.TestCase):
    """
    ======== here comes unittests for tasks 1-10 ========
    """

    def test_task1_common_elements(self):
        input_list = [
            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
            [1, 1, 5, 3, 2, 13, 8, 21, 34, 55, 89]
        ]
        check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        result = [1, 2, 3, 5, 8, 13]
        for elem in input_list:
            with self.subTest(i=elem):
                self.assertEqual(task1_common_elements(elem, check_list),
                                 result)

    def test_task1_common_elements_empty(self):
        input_list = [
            [],
            [14, 15, 16, 17]
        ]
        check_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        result = []
        for elem in input_list:
            with self.subTest(i=elem):
                self.assertEqual(task1_common_elements(elem, check_list),
                                 result)

    def test_task2_letter_times(self):
        list_strings = [
            ('I am a good developer. I am also a writer', 5),
            ('I am a good developer', 2),
            ('good developer', 0)
        ]
        for string, result in list_strings:
            with self.subTest(string=string):
                self.assertEqual(task2_letter_times(string), result)

    def test_task3_is_power_true(self):
        numbers = [9, 27, 3]
        for elem in numbers:
            with self.subTest(i=elem):
                self.assertTrue(task3_is_power(elem))

    def test_task3_is_power_false(self):
        numbers = [6, 7, 15, 0]
        for elem in numbers:
            with self.subTest(i=elem):
                self.assertFalse(task3_is_power(elem))

    def test_task4_add_repeatedly(self):
        lst = [
            (59, 5),
            (48, 3),
            (5, 5)
        ]
        for number, result in lst:
            with self.subTest(i=number):
                self.assertEqual(task4_add_repeatedly(number), result)

    def test_task5_push_zeros(self):
        lst = [
            ([0, 2, 3, 4, 6, 7, 10], [2, 3, 4, 6, 7, 10, 0]),
            ([0, 2, 0, 4, 0, 0, 10], [2, 4, 10, 0, 0, 0, 0])
        ]
        for check, result in lst:
            with self.subTest(i=check):
                self.assertEqual(task5_push_zeros(check), result)

    def test_task6_arithmetic_progression_check(self):
        inputs = [
            [2, 4, 6, 8, 10],
            [5, 10, 15, 20, 25],
            [5.5, 11, 16.5, 22],
        ]
        for elem in inputs:
            with self.subTest(i=elem):
                self.assertTrue(task6_arithmetic_progression_check(elem))
        input1 = [5, 10, 15, 20, 20]
        with self.subTest(i=input1):
            self.assertFalse(task6_arithmetic_progression_check(input1))

    def test_task7_unique_number(self):
        lst = [
            ([4, 3, 5, 3, 4], [5]),
            ([2], [2]),
            ([5, 3, 3, 3, 4], [5, 4]),
            ([5, 3, 5, 3, 4, 4], [])
        ]
        for check, result in lst:
            with self.subTest(i=check):
                self.assertEqual(task7_unique_number(check), result)

    def test_task8_missing_number(self):
        lst = [
            ([1, 2, 3, 4, 6, 7, 8], [5]),
            ([1, 2, 4, 6, 7, 8], [3, 5]),
            ([1, 2, 3, 4, 5, 6, 7, 8], [])
        ]
        for check, result in lst:
            with self.subTest(i=check):
                self.assertEqual(task8_missing_number(check), result)

    def test_task9_find_before_tuple(self):
        lst = [1, 2, 3, (1, 2), 3]
        with self.subTest(lst):
            self.assertEqual(task9_find_before_tuple(lst), 3)
        list_a = [
            [1, 2, 3, 3],
            []
        ]
        for elem in list_a:
            with self.subTest(i=elem):
                self.assertEqual(task9_find_before_tuple(list_a), 0)

    def test_task10_string_reversed(self):
        lst = [
            ('Hello World and Coders', 'sredoC dna dlroW olleH'),
            ("Hello World", 'dlroW olleH')
        ]
        for check, result in lst:
            with self.subTest(i=check):
                self.assertEqual(task10_string_reversed(check), result)


if __name__ == '__main__':
    unittest.main()
