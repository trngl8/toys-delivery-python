class Courier:

    def __init__(self):
        self.name = 'Morooze'
        self.cape_color = 'red'
        self.bread = True
        self.partners = []

    def get_name(self):
        return self.name


obj = Courier()
print(f'Name: {obj.get_name()}')


