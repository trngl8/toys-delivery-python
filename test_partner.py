import unittest
from models import Partner
from models import DeliveryList as Childrenlist


class TestPartner(unittest.TestCase):

    def test_get_list(self):
        children_list = Childrenlist()
        children_list.add('Test Name', '4, The Main str.', 1)
        children_list.add('Other Name', '2, The Second str.', 2)
        grandchild = Partner('Snegurochka', children_list)

        last_item = grandchild.get_list().last()

        self.assertEqual('2, The Second str.', last_item['ADDRESS'])


if __name__ == '__main__':
    unittest.main()
