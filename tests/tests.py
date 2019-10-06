import unittest

from .homework import Rectangle


class TestCases(unittest.TestCase):
    rect1 = Rectangle(3, 4)

    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.rect1.get_rectangle_perimeter(), 14)

    def test_get_rectangle_square(self):
        self.assertEqual(self.rect1.get_rectangle_square(), 12)

    def test_get_sum_of_corners_result(self):
        for i in [1, 2, 3, 4]:
            self.assertEqual(self.rect1.get_sum_of_corners(i), i * 90)

    def test_get_sum_of_corners_raises(self):
        self.assertRaises(ValueError, self.rect1.get_sum_of_corners, 5)

    def test_get_rectangle_diagonal(self):
        self.assertEqual(self.rect1.get_rectangle_diagonal(), 5)

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.rect1.get_radius_of_circumscribed_circle(), 2.5)

    def test_get_radius_of_inscribed_circle_result(self):
        self.rect2 = Rectangle(4, 4)
        self.assertEqual(self.rect2.get_radius_of_inscribed_circle(), 2)

    def test_get_radius_of_inscribed_circle_raises(self):
        self.assertRaises(ValueError, self.rect1.get_radius_of_inscribed_circle)


if __name__ == "__main__":
    unittest.main()