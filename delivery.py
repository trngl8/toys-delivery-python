import datetime


class Courier:

    def __init__(self, culture):
        self.culture = culture
        self.name = 'Morooze'
        self.cape_color = 'red'
        self.bread = True
        self.partners = []

    def get_name(self):
        return self.name

    def get_partners_count(self):
        if self.culture == 'USSR':
            return 1
        return 0

    def can_work(self):
        now = datetime.date
        # TODO: implement date check
        return False


class Vehicle:

    def __init__(self, v_type):
        self.v_type = v_type
        self.speed = 1
        self.position = 1

    def move(self, position):
        self.position += position


obj = Courier('USSR')
print(f'Name: {obj.get_name()}, can work: {obj.can_work()}')
