from models import Courier
from models import CourierExtended
from models import Vehicle
from models import Sledge
from models import DeliveryList
from models import Partner
from models import PartnerExtended

# USSR culture
courier  = Courier('USSR', 'Mooroze', 'blue')
v8 = Vehicle('truck')
print(f'Name: {courier.get_name()}, can work: {courier.can_work()}')

child_list = DeliveryList()
child_list.add('Theo', '7172', 3)
child_list.add('One', '101', 1)
child_list.add('Two', '000', 2)

courier_partner = Partner("USSR", child_list)

# USA culture
obj = CourierExtended('USA', 'Santa Claus', 'red')
transport = Sledge('sled')
print(f'Name: {obj.get_name()}, can work: {obj.can_work()}')

courier_extended_partner = PartnerExtended("USA", child_list)

courier.add_partner(courier_partner)

delivery_targets = courier_partner.get_list().delivery_list

if not obj.can_work():
    print("Delivery is unavailable")
    exit

while delivery_targets:
    next_delivery = delivery_targets.pop()
    result = courier.delivery_run(next_delivery)
    print(f"Delivered by {result} seconds")



