from Classes.Customer import Customer
from Product import Product

class Order:

    def __init__(self, customer, dict_of_products=None):
        self.customer = customer
        self.products = dict_of_products
        pass

    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, value):
        if not isinstance(value, Customer):
            raise TypeError
        self.__customer = value

    @property
    def products(self):
        return list(map(str, self.__products))

    @property
    def order(self):
        return f"User: {self.__customer}| Orders: {self.products}"

    @products.setter
    def products(self, value):
        if list(map(lambda temp: isinstance(temp, Product), value.keys())).__contains__(False):
            raise TypeError
        if list(map(lambda temp: temp <= 0, value.values())).__contains__(True):
            raise ValueError
        self.__products = value

    @property
    def total_value(self):
        return self.get_total_value()

    def get_total_value(self) -> int:
        temp = 0
        for product in self.__products:
            temp += product.price * self.__products[product]
        return temp

    def check_if_affordable(self):
        return self.get_total_value() < self.__customer.currency
        # if self.get_total_value() < self.__customer.currency:
        #     return True
        # return False

    def add_product(self, value):
        if not isinstance(value, dict):
            raise TypeError
        if not isinstance(list(value.keys())[0], Product):
            return TypeError
        if not isinstance(list(value.values())[0], int):
            return TypeError
        if list(value.values())[0] <= 0:
            raise ValueError
        self.__products[list(value.keys())[0]] = list(value.values())[0]

    def del_product(self, id):
        for item in list(self.__products.keys()):
            if item.Id == id:
                self.__products.pop(item)
                break
