import unittest
from models import Courier
from models import CourierExtended


class TestCourier(unittest.TestCase):

    def test_move(self):
        glovo = Courier("kubernetes", 'Santa', 'red')
        result = glovo.delivery("fast")
        self.assertEqual(True, result)

    def test_name(self):
        target = Courier("test1", "test2", 'test3')
        result = target.get_name()
        self.assertEqual("test2", result)

    def test_get_full_name(self):
        target = Courier("USSR", "Morooze", 'Blue')
        result = target.get_full_name()
        self.assertEqual("Blue Morooze", result)

class TestCourierExtended(unittest.TestCase):
    def test_name(self):
        target = CourierExtended("USA", "Santa Claus", 'red')
        result = target.get_name()
        self.assertEqual("Santa Claus", result)

    def test_cape_color(self):
        target = CourierExtended("USA", "Santa Claus", 'red')
        result = target.cape_color
        self.assertEqual("red", result)

    def test_get_partners_count(self):
        target = CourierExtended("USA", "Santa Claus", 'red')
        result = target.get_partners_count()
        self.assertEqual(100, result)


if __name__ == '__main__':
    unittest.main()
