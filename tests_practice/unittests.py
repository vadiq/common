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
        list_a = [
            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
            [1, 1, 5, 3, 2, 13, 8, 21, 34, 55, 89]
        ]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        c = [1, 2, 3, 5, 8, 13]
        for i in list_a:
            with self.subTest(i=i):
                self.assertEqual(task1_common_elements(i, b), c)
        a1 = [14, 15, 16, 17]
        with self.subTest(a1):
            self.assertIsNone(task1_common_elements(a1, b))

    def test_task2_letter_times(self):
        list_s = [
            ('I am a good developer. I am also a writer', 5),
            ('I am a good developer', 2),
            ('good developer', 0)
        ]
        for s1, s2 in list_s:
            with self.subTest(s1=s1):
                self.assertEqual(task2_letter_times(s1), s2)

    def test_task3_is_power(self):
        a = [9, 27, 3]
        for i in a:
            with self.subTest(i=i):
                self.assertTrue(task3_is_power(i))
        a = [6, 7, 15, 0]
        for j in a:
            with self.subTest(j=j):
                self.assertFalse(task3_is_power(j))

    def test_task4_add_repeatedly(self):
        lst = [
            (59, 5),
            (48, 3),
            (5, 5)
        ]
        for i, j in lst:
            with self.subTest(i=i):
                self.assertEqual(task4_add_repeatedly(i), j)

    def test_task5_push_zeros(self):
        lst = [
            ([0, 2, 3, 4, 6, 7, 10], [2, 3, 4, 6, 7, 10, 0]),
            ([0, 2, 0, 4, 0, 0, 10], [2, 4, 10, 0, 0, 0, 0])
        ]
        for a, b in lst:
            with self.subTest(a=a):
                self.assertEqual(task5_push_zeros(a), b)

    def test_task6_arithmetic_progression_check(self):
        list_a = [
            [2, 4, 6, 8, 10],
            [5, 10, 15, 20, 25],
            [5.5, 11, 16.5, 22],
        ]
        for i in list_a:
            with self.subTest(i=i):
                self.assertTrue(task6_arithmetic_progression_check(i))
        a = [5, 10, 15, 20, 20]
        with self.subTest(a):
            self.assertFalse(task6_arithmetic_progression_check(a))

    def test_task7_unique_number(self):
        lst = [
            ([4, 3, 5, 3, 4], 5),
            ([2], 2),
            ([5, 3, 3, 3, 4], [5, 4])
        ]
        for i, j in lst:
            with self.subTest(i=i):
                self.assertEqual(task7_unique_number(i), j)
        lst = [
            [5, 3, 5, 3, 4, 4],
            []
        ]
        for j in lst:
            with self.subTest(j=j):
                self.assertIsNone(task7_unique_number(j))

    def test_task8_missing_number(self):
        lst = [
            ([1, 2, 3, 4, 6, 7, 8], 5),
            ([1, 2, 4, 6, 7, 8], [3, 5])
        ]
        for i, j in lst:
            with self.subTest(i=i):
                self.assertEqual(task8_missing_number(i), j)
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        with self.subTest(a):
            self.assertIsNone(task8_missing_number(a))

    def test_task9_find_before_tuple(self):
        a = [1, 2, 3, (1, 2), 3]
        with self.subTest(a):
            self.assertEqual(task9_find_before_tuple(a), 3)
        list_a = [
            [1, 2, 3, 3],
            []
        ]
        for i in list_a:
            with self.subTest(i=i):
                self.assertIsNone(task9_find_before_tuple(i))

    def test_task10_string_reversed(self):
        lst = [
            ('Hello World and Coders', 'sredoC dna dlroW olleH'),
            ("Hello World", 'dlroW olleH')
        ]
        for i, j in lst:
            with self.subTest(i=i):
                self.assertEqual(task10_string_reversed(i), j)


if __name__ == '__main__':
    unittest.main()
