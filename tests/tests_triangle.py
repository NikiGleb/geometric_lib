import unittest

from triangle import area, perimeter

class TriangleTestCase(unittest.TestCase):

    # area
    def test_area_1(self):
        res = area(6, 4)
        self.assertEqual(res, 12.0)

    def test_area_2(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_3(self):
        res = area(5, 3.2)
        self.assertAlmostEqual(res, 8.0)

    # perimeter
    def test_perimeter_1(self):
        res = perimeter(3, 4, 5)
        self.assertEqual(res, 12)

    def test_perimeter_2(self):
        res = perimeter(5, 5, 5)
        self.assertEqual(res, 15)

    def test_perimeter_3(self):
        res = perimeter(0, 0, 0)
        self.assertEqual(res, 0)


if __name__ == '__main__':
    unittest.main()
