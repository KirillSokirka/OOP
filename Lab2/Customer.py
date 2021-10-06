import re


class Customer:

    def __init__(self, name, surname, phone_number, currency, *args):
        self.name = name
        self.surname = surname
        self.phone_number = phone_number
        self.currency = currency

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def surname(self):
        return self.__surname

    @surname.setter
    def surname(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__surname = value

    def get_fullname(self):
        return f"{self.__name} {self.__surname}"

    @property
    def phone_number(self):
        return self.__name

    @phone_number.setter
    def phone_number(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not self.__validate_phone(value):
            raise ValueError
        self.__phone = value

    def __validate_phone(self, value):
        rule = re.compile("^\+[0-9]{3}\((\d{2})\)-\d{3}-\d{2}-\d{2}")
        if rule.match(value):
            return True
        return False

    @property
    def currency(self):
        return self.__currency

    @currency.setter
    def currency(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value < 0:
            raise ValueError
        self.__currency = value
