from Customer import Customer
from Product import Product

class Order:

    def __init__(self, customer, *args):
        self.customer = customer
        self.products = list(args)
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

    @products.setter
    def products(self, value):
        if list(map(lambda temp: isinstance(temp, Product), value)).__contains__(False):
            raise TypeError
        self.__products = value

    @property
    def total_value(self):
        return self.get_total_value()

    def get_total_value(self) -> int:
        temp = 0
        for product in self.__products:
            temp += product.price * product.quantity
        return temp

    def check_if_affordable(self):
        if self.get_total_value() < self.__customer.currency:
            return True
        return False

    def add_product(self, value):
        if not isinstance(value, Product):
            raise TypeError
        self.__products.append(value)

    def del_product(self, id):
        for item in self.__products:
            if item.Id == id:
                self.__products.remove(item)
