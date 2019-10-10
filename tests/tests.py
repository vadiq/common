import unittest

from .homework import Rectangle


class TestCases(unittest.TestCase):
    rect1 = Rectangle(3, 4)
    rect2 = Rectangle(12, 5)
    rect3 = Rectangle(0, 4)

    def test_get_rectangle_perimeter(self):
        self.assertEqual(self.rect1.get_rectangle_perimeter(), 14)
        self.assertEqual(self.rect2.get_rectangle_perimeter(), 14)
        self.assertEqual(self.rect3.get_rectangle_perimeter(), 0)

    def test_get_rectangle_square(self):
        self.assertEqual(self.rect1.get_rectangle_square(), 12)
        self.assertEqual(self.rect2.get_rectangle_square(), 60)
        self.assertEqual(self.rect3.get_rectangle_square(), 0)

    def test_get_sum_of_corners_result(self):
        for i in range(1, 5):
            self.assertEqual(self.rect1.get_sum_of_corners(i), i * 90)
            self.assertEqual(self.rect2.get_sum_of_corners(i), i * 90)
            self.assertEqual(self.rect3.get_sum_of_corners(i), 0 * 90)

    def test_get_sum_of_corners_raises(self):
        with self.assertRaises(ValueError):
            self.rect1.get_sum_of_corners(5)
            self.rect2.get_sum_of_corners(10)
            self.rect3.get_sum_of_corners(0)
            self.rect3.get_sum_of_corners(-2)

    def test_get_rectangle_diagonal(self):
        self.assertEqual(self.rect1.get_rectangle_diagonal(), 5)
        self.assertEqual(self.rect2.get_rectangle_diagonal(), 13)
        self.assertEqual(self.rect3.get_rectangle_diagonal(), 0)

    def test_get_radius_of_circumscribed_circle(self):
        self.assertEqual(self.rect1.get_radius_of_circumscribed_circle(), 2.5)
        self.assertEqual(self.rect2.get_radius_of_circumscribed_circle(), 6.5)
        self.assertEqual(self.rect3.get_radius_of_circumscribed_circle(), 0)

    def test_get_radius_of_inscribed_circle_result(self):
        self.assertEqual(Rectangle(16, 16).get_radius_of_inscribed_circle(), 8)
        self.assertEqual(Rectangle(6, 6).get_radius_of_inscribed_circle(), 3)

    def test_get_radius_of_inscribed_circle_raises(self):
        with self.assertRaises(ValueError):
            self.rect1.get_radius_of_inscribed_circle()
            Rectangle(6, -2).get_radius_of_inscribed_circle()


if __name__ == "__main__":
    unittest.main()
