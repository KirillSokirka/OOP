from models.Pizza import Pizza
from json_files.json_worker import JSONWorker

import calendar
from datetime import date

class PizzaOfTheDay(Pizza):

    def __init__(self, name, price, ingredients, day):
        super(PizzaOfTheDay, self).__init__(name, price, ingredients)
        self.day = day

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if not isinstance(value, int):
            raise TypeError
        if not value in range(7):
            raise ValueError
        self.__day = value

    @staticmethod
    def get_pizza_of_the_day(day):
        if not day in range(7):
            raise IndexError
        _pizza = JSONWorker.get_object_by_key('json_files/pizza_of_the_day.json', 'day', day)
        return PizzaOfTheDay(**_pizza)

    def __str__(self):
        return super(PizzaOfTheDay, self).__str__() + \
               f'\n\tday - {calendar.day_name[self.__day]}'

    def __dict__(self):
        temp = super(PizzaOfTheDay, self).__dict__()
        temp['day'] = self.__day
        return temp

