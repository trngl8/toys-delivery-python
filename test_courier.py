import unittest
from models import Courier


class TestCourier(unittest.TestCase):

    def test_move(self):
        glovo = Courier("kubernetes")
        result = glovo.delivery("fast")
        self.assertEqual(True, result)


if __name__ == '__main__':
    unittest.main()
