import unittest
import math

from circle import area, perimeter

class CircleTestCase(unittest.TestCase):

    # area
    def test_area_1(self):
        res = area(2)
        self.assertAlmostEqual(res, math.pi * 4)

    def test_area_2(self):
        res = area(0)
        self.assertEqual(res, 0)

    def test_area_3(self):
        res = area(1)
        self.assertAlmostEqual(res, math.pi)

    # perimeter 
    def test_perimeter_1(self):
        res = perimeter(2)
        self.assertAlmostEqual(res, math.pi * 4)

    def test_perimeter_2(self):
        res = perimeter(0)
        self.assertEqual(res, 0)

    def test_perimeter_3(self):
        res = perimeter(1)
        self.assertAlmostEqual(res, 2 * math.pi)


if __name__ == '__main__':
    unittest.main()
