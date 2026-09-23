import unittest

from rectangle import area, perimeter

class RectangleTestCase(unittest.TestCase):

    # area
    def test_area_1(self):
        res = area(3, 4)
        self.assertEqual(res, 12)

    def test_area_2(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_area_3(self):
        res = area(10, 10)
        self.assertEqual(res, 100)

    # perimeter 
    def test_perimeter_1(self):
        res = perimeter(3, 4)
        self.assertEqual(res, 14)

    def test_perimeter_2(self):
        res = perimeter(0, 0)
        self.assertEqual(res, 0)

    def test_perimeter_3(self):
        res = perimeter(5, 5)
        self.assertEqual(res, 20)


if __name__ == '__main__':
    unittest.main()
