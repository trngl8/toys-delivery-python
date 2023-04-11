import unittest
from models import Courier


class TestCourier(unittest.TestCase):

    def test_move(self):
        glovo = Courier("kubernetes", 'Santa', 'red')
        result = glovo.delivery("fast")
        self.assertEqual(True, result)

    def test_name(self):
        target = Courier("test1", "test2", 'test3')
        result = target.get_name()
        self.assertEqual("test2", result)


if __name__ == '__main__':
    unittest.main()
