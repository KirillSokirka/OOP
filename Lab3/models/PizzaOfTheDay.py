from models.Pizza import Pizza
from json_worker import JSONWorker

import calendar


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

    def __str__(self):
        return super(PizzaOfTheDay, self).__str__() + \
               f'\n\tday - {calendar.day_name[self.__day]}'

    def __dict__(self):
        temp = super(PizzaOfTheDay, self).__dict__()
        temp['day'] = self.__day
        return temp

