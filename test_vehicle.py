import unittest
from models import Vehicle
from models import Sledge


class TestVehicle(unittest.TestCase):

    def test_move(self):
        v8 = Vehicle('camaro', 8)
        v8.move(3)
        self.assertEqual(25, v8.position)

    def test_sledge(self):
        sledge = Sledge('sled')
        result = len(sledge.get_engine())
        self.assertEqual(9, result)


# entry point
if __name__ == '__main__':
    unittest.main()
