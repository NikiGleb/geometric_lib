import unittest

from square import area, perimeter

class SquareTestCase(unittest.TestCase):

    # area
    def test_area_1(self):
        res = area(5)
        self.assertEqual(res, 25)

    def test_area_2(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_3(self):
        res = area(2.5)
        self.assertAlmostEqual(res, 6.25)

    # perimeter
    def test_perimeter_1(self):
        res = perimeter(5)
        self.assertEqual(res, 20)

    def test_perimeter_2(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_3(self):
        res = perimeter(2.5)
        self.assertAlmostEqual(res, 10.0)


if __name__ == '__main__':
    unittest.main()
