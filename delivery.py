from models import Courier
from models import Vehicle
from models import Childrenlist
from models import Partner


obj = Courier('USSR')
v8 = Vehicle('truck')
print(f'Name: {obj.get_name()}, can work: {obj.can_work()}')

child1 = Childrenlist(1, 'Vasya', 'Bashirkastan', 3)
child2 = Childrenlist(2, 'Olya', 'Vladivostok', 2)
child3 = Childrenlist(3, 'Sanya', 'Moskva', 1)

grand_child = Partner("Snegurochka", child1)
