import unittest
from models import Partner


class TestPartner(unittest.TestCase):

    def test_get_list(self):
        grandchild = Partner
        # TODO: implement test list
        self.assertIsInstance(grandchild.get_list, list)  # TODO: check the correct classname


if __name__ == '__main__':
    unittest.main()
