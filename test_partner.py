import unittest
from models import Partner
from models import Childrenlist


class TestPartner(unittest.TestCase):

    def test_get_list(self):
        # TODO: choose better name for the "list" structure
        children_list = Childrenlist(2, 'Olya', 'Vladivostok', 2)
        grandchild = Partner('Sneg', children_list)
        self.assertEqual('Olya', grandchild.get_list().get_name())


if __name__ == '__main__':
    unittest.main()
