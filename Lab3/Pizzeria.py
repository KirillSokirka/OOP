from json_worker import JSONWorker
from models.Pizza import Pizza
from models.PizzaOfTheDay import PizzaOfTheDay


class Pizzeria:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value or value.strip() == '':
            raise ValueError
        self.__name = value

    def get_pizza_of_the_day(self, day):
        if not day in range(7):
            raise IndexError
        _pizza = JSONWorker.get_object_by_key('json_files/pizza_of_the_day.json', 'day', day)
        return PizzaOfTheDay(**_pizza)

    def get_standart_pizza(self, name):
        if not isinstance(name, str):
            raise TypeError
        if not name or name.strip() == '':
            raise ValueError
        if not name in JSONWorker.get_values_by_parameter_name('json_files/menu.json', 'name'):
            return None
        return Pizza(**JSONWorker.get_object_by_key('json_files/menu.json', 'name', name))

    def get_standart_menu(self):
        list_pizza_dicts = JSONWorker.get_all_objects('json_files/menu.json')
        list_of_pizza = []
        for p_dict in list_pizza_dicts:
            list_of_pizza.append(Pizza(**p_dict))
        return list_of_pizza

    def add_your_custom_pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError
        names = JSONWorker.get_values_by_parameter_name('json_files/menu.json', 'name')
        if pizza.name in names:
            raise ValueError('This pizza already exists in menu')
        JSONWorker.save_to_json('json_files/menu.json', pizza)

    def order_pizza(self, pizza):
        if not isinstance(pizza, Pizza):
            raise TypeError
        if not pizza.name in JSONWorker.get_values_by_parameter_name('json_files/menu.json', 'name'):
            if not pizza.name in JSONWorker.get_values_by_parameter_name('json_files/pizza_of_the_day.json', 'name'):
                return False
        return True
