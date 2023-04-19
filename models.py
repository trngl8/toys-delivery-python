import datetime


class Courier:

    def __init__(self, culture, name, cape_color):
        self.culture = culture
        self.name = name
        self.cape_color = cape_color
        self.bread = True
        self.partners = []
        self.level = 1
        self.delivery_type = 'fast'

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

    def delivery(self, delivery_type):
        self.delivery_type = delivery_type
        return True

    def next_delivery(self):
        # TODO: add a fibonnacci sequence
        self.level += 1


class Vehicle:

    def __init__(self, v_type, speed):
        self.v_type = v_type
        self.speed = speed
        self.position = 1

    def move(self, position):
        self.position += position * self.speed


class Partner:
    def __init__(self, culture, list):
        self.culture = culture
        self.name = 'Snegurochka'
        self.partners = []
        self.children_list = list

    def get_list(self):
        return self.children_list


class DeliveryList:
    def __init__(self):
        self.delivery_list = []
        self.pointer = 0

    def add(self, name, address, toy_id):
        next_pointer = self.pointer + 1
        self.delivery_list.append({
            'ID': next_pointer,
            'NAME': name,
            'ADDRESS': address,
            'TOY_ID': toy_id
        })
        self.pointer = next_pointer

    def last(self):
        return self.delivery_list.pop()
