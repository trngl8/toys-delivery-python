class Courier:

    def __init__(self):
        self.name = 'Morooze'
        self.cape_color = 'red'
        self.bread = True
        self.partners = []

    def get_name(self):
        return self.name


class Vehicle:

    def __init__(self, v_type):
        self.v_type = v_type
        self.speed = 1
        self.position = 1

    def move(self, position):
        self.position += position


obj = Courier()
print(f'Name: {obj.get_name()}')


