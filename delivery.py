from models import Courier
from models import Vehicle


obj = Courier('USSR')
v8 = Vehicle('truck')
print(f'Name: {obj.get_name()}, can work: {obj.can_work()}')
