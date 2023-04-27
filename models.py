import datetime


class Courier:
    """ Base deliverer """

    def __init__(self, culture, name, cape_color):
        self.__culture = culture
        self.__name = name
        self.__cape_color = cape_color
        self.__bread = True
        self.__partners = []
        self.__level = 1
        self.__delivery_type = 'fast'

    def get_name(self):
        """ Getter for name """
        return self.__name

    def get_full_name(self):
        """ Getter for full name """
        return f"{self.__cape_color} {self.__name}"

    def get_partners_count(self):
        """ Getter partners count """
        if self.__culture == 'USSR':
            return 1
        return 0

    def can_work(self):
        """ Check work ability """
        now = datetime.datetime.now().time()
        start_time = datetime.time(5, 0)
        end_time = datetime.time(21, 0)

        if start_time <= now <= end_time:
            return True
        else:
            return False

    def set_delivery_type(self, delivery_type):
        """ Set delivery type """
        self.delivery_type = delivery_type
        return True

    def add_partner(self, partner):
        self.__partners.append(partner)

    def next_delivery(self):
        """ Increase difficulty lever """
        self.__level += 1

    def delivery_run(self, delivery_target):
        """ Run delivery process """
        self.next_delivery()
        result_speed = delivery_target.get('ID') * self.__level

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

    def __init__(self, v_type, speed):
        self.v_type = v_type
        self.speed = speed
        self.position = 1

    def move(self, position):
        self.position += position * self.speed


class Sledge:

    def __init__(self, v_type, deer_names):
        self.v_type = v_type
        self.speed = 150
        self.position = 1
        self.deer_names = ["Salmon", "Baget", "Zvezda", "Tank", "Gagarin", "Molot", "Tulya", "Sneg", "Rasmus"]
    def move(self, position):
        self.position += position

    def get_engine(self):
        # TODO: implement business logic
        return range(0, 1)


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
