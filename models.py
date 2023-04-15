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

    def add_partner(self, partner):
        self.partners.append(partner)

    def next_delivery(self):
        # TODO: add a fibonnacci sequence
        self.level += 1

    def delivery_run(self, delivery_target):
        # TODO: use vehicle to increase speed
        self.next_delivery()
        result_speed = delivery_target.get('ID') * self.level

        return result_speed


class CourierExtended:

    def __init__(self, culture, name, cape_color):
        self._culture = culture
        self.name = name
        self.cape_color = cape_color
        self.bread = True
        self.partners = []
        self.level = 1
        self.delivery_type = 'fast'

    def get_name(self):
        return self.name

    def get_partners_count(self):
        return 100

    def can_work(self):
        return True


class Vehicle:

    def __init__(self, v_type):
        self.v_type = v_type
        self.speed = 1
        self.position = 1

    def move(self, position):
        self.position += position


class Sledge:

    def __init__(self, v_type):
        self.v_type = v_type
        self.speed = 150
        self.position = 1

    def move(self, position):
        self.position += position


class Partner:
    def __init__(self, culture, list):
        self.culture = culture
        self.name = 'Snegurochka'
        self.partners = []
        self.children_list = list

    def get_name(self):
        return self.name

    def get_list(self):
        return self.children_list


class PartnerExtended(Partner):

    def __init__(self, culture, list):
        super().__init__(culture, list)
        self.name = 'Gnome'


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
