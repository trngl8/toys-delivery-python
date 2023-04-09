from models import Courier
from models import Vehicle
from models import DeliveryList
from models import Partner


obj = Courier('USSR')
v8 = Vehicle('truck')
print(f'Name: {obj.get_name()}, can work: {obj.can_work()}')

child_list = DeliveryList()
child_list.add('Theo', '7172', 3)
child_list.add('One', '101', 1)

courier_partner = Partner("USSR", child_list)
