import unittest
from models import Courier
from models import Partner
from models import CourierExtended
from models import DeliveryList


class TestCourier(unittest.TestCase):

    def test_move(self):
        glovo = Courier("kubernetes", 'Santa', 'red')
        result = glovo.set_delivery_type("fast")
        self.assertEqual(True, result)

    def test_name(self):
        target = Courier("test1", "test2", 'test3')
        result = target.get_name()
        self.assertEqual("test2", result)

    def test_get_full_name(self):
        target = Courier("USSR", "Morooze", 'Blue')
        result = target.get_full_name()
        self.assertEqual("Blue Morooze", result)

    def test_delivery_run(self):
        target = Courier("USSR", "Morooze", 'Blue')
        children_list = DeliveryList()
        children_list.add('Test Name', '4, The Main str.', 1)
        children_list.add('Other Name', '2, The Second str.', 2)
        courier_partner = Partner("USSR", children_list)

        target.add_partner(courier_partner)
        result = target.delivery_run(courier_partner.get_list().delivery_list.pop())
        self.assertEqual(4, result)

    def test_get_partners_count(self):
        target = Courier("USSR", "Morooze", 'Blue')
        children_list = DeliveryList()
        children_list.add('Test Name', '4, The Main str.', 1)
        children_list.add('Other Name', '2, The Second str.', 2)
        courier_partner = Partner("USSR", children_list)

        target.add_partner(courier_partner)

        self.assertEqual(1, target.get_partners_count())

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
