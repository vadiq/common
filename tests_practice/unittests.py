import unittest

from tests_practice.definitions import (
    task1,
    task2,
    task3,
    task4,
    task5,
    task6,
    task7,
    task8,
    task9,
    task10
)


class TestCases(unittest.TestCase):
    """
    ======== here comes unittests for tasks 1-10 ========
    """

    def test_task1(self):
        list_a = [
            [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89],
            [1, 1, 5, 3, 2, 13, 8, 21, 34, 55, 89]
        ]
        b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        c = [1, 2, 3, 5, 8, 13]
        for i in list_a:
            with self.subTest(i=i):
                self.assertEqual(task1(i, b), c)
        a1 = [14, 15, 16, 17]
        with self.subTest(a1):
            self.assertIsNone(task1(a1, b))

    def test_task2(self):
        list_s = [
            ('I am a good developer. I am also a writer', 5),
            ('I am a good developer', 2),
            ('good developer', 0)
        ]
        for s1, s2 in list_s:
            with self.subTest(s1=s1):
                self.assertEqual(task2(s1), s2)

    def test_task3(self):
        a = [9, 27, 3]
        for i in a:
            with self.subTest(i=i):
                self.assertEqual(task3(i), 3)
        a = [6, 7, 15, 0]
        for j in a:
            with self.subTest(j=j):
                self.assertNotEqual(task3(j), 3)

    def test_task4(self):
        lst = [
            (59, 5),
            (48, 3),
            (5, 5)
        ]
        for i, j in lst:
            with self.subTest(i=i):
                self.assertEqual(task4(i), j)

    def test_task5(self):
        lst = [
            ([0, 2, 3, 4, 6, 7, 10], [2, 3, 4, 6, 7, 10, 0]),
            ([0, 2, 0, 4, 0, 0, 10], [2, 4, 10, 0, 0, 0, 0])
        ]
        for a, b in lst:
            with self.subTest(a=a):
                self.assertEqual(task5(a), b)

    def test_task6(self):
        list_a = [
            [2, 4, 6, 8, 10],
            [5, 10, 15, 20, 25],
            [5.5, 11, 16.5, 22],
        ]
        for i in list_a:
            with self.subTest(i=i):
                self.assertTrue(task6(i))
        a = [5, 10, 15, 20, 20]
        with self.subTest(a):
            self.assertFalse(task6(a))

    def test_task7(self):
        lst = [
            ([4, 3, 5, 3, 4], 5),
            ([2], 2),
            ([5, 3, 3, 3, 4], [5, 4])
        ]
        for i, j in lst:
            with self.subTest(i=i):
                self.assertEqual(task7(i), j)
        lst = [
            [5, 3, 5, 3, 4, 4],
            []
        ]
        for j in lst:
            with self.subTest(j=j):
                self.assertIsNone(task7(j))

    def test_task8(self):
        lst = [
            ([1, 2, 3, 4, 6, 7, 8], 5),
            ([1, 2, 4, 6, 7, 8], [3, 5])
        ]
        for i, j in lst:
            with self.subTest(i=i):
                self.assertEqual(task8(i), j)
        a = [1, 2, 3, 4, 5, 6, 7, 8]
        with self.subTest(a):
            self.assertIsNone(task8(a))

    def test_task9(self):
        a = [1, 2, 3, (1, 2), 3]
        with self.subTest(a):
            self.assertEqual(task9(a), 3)
        list_a = [
            [1, 2, 3, 3],
            []
        ]
        for i in list_a:
            with self.subTest(i=i):
                self.assertIsNone(task9(i))

    def test_task10(self):
        lst = [
            ('Hello World and Coders', 'sredoC dna dlroW olleH'),
            ("Hello World", 'dlroW olleH')
        ]
        for i, j in lst:
            with self.subTest(i=i):
                self.assertEqual(task10(i), j)


if __name__ == '__main__':
    unittest.main()
