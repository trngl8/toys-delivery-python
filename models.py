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
        now = datetime.datetime.now().time()
        start_time = datetime.time(5, 0)
        end_time = datetime.time(21, 0)

        if start_time <= now <= end_time:
            return True
        else:
            return False


class Vehicle:

    def __init__(self, v_type):
        self.v_type = v_type
        self.speed = 1
        self.position = 1

    def move(self, position):
        self.position += position


class Partner:
    def __init__(self, culture, list):
        self.culture = culture
        self.name = 'Snegurochka'
        self.partners = []
        self.children_list = list

    def get_list(self):
        return self.children_list


class Childrenlist:
    def __init__(self, id, name, address, toy_id):
        self.id = id
        self.name = name
        self.address = address
        self.toy_id = toy_id

    def get_name(self):
        return self.name

    def __str__(self):
        return f"ID: {self.id}, NAME: {self.name}, ADDRESS: {self.address}, TOY_ID: {self.toy_id}"
