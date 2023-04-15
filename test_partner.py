import unittest
from models import Partner
from models import PartnerExtended
from models import DeliveryList


class TestPartner(unittest.TestCase):

    def test_get_list(self):
        children_list = DeliveryList()
        children_list.add('Test Name', '4, The Main str.', 1)
        children_list.add('Other Name', '2, The Second str.', 2)
        grandchild = Partner('USSR', children_list)

        last_item = grandchild.get_list().last()

        self.assertEqual('2, The Second str.', last_item['ADDRESS'])


class TestPartnerExtended(unittest.TestCase):

    def test_get_list(self):
        children_list = DeliveryList()
        children_list.add('Test Name', '4, The Main str.', 1)
        children_list.add('Other Name', '2, The Second str.', 2)
        grandchild = PartnerExtended('USA', children_list)

        last_item = grandchild.get_list().last()

        self.assertEqual('2, The Second str.', last_item['ADDRESS'])


if __name__ == '__main__':
    unittest.main()
