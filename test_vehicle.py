import unittest
from models import Vehicle


class TestVehicle(unittest.TestCase):

    def test_move(self):
        # TODO: does vehicle speed depends on something?
        # TODO: add a argument to the constructor
        v8 = Vehicle('camaro')
        v8.move(3)
        self.assertEqual(25, v8.position)


# entry point
if __name__ == '__main__':
    unittest.main()
