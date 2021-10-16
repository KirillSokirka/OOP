from Product import Product


class ItemModel:

    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    @property
    def product(self):
        return self.__product

    @product.setter
    def product(self, value):
        if not isinstance(value, Product):
            raise TypeError
        self.__product = value

    @property
    def quantity(self):
        return self.__quantity

    @quantity.setter
    def quantity(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        self.__quantity = value

    def __str__(self):
        return f"Name: {self.product.name}\n\tDescription: {self.product.description}\n\t" \
               f"Price: {self.product.price}\n\tDimension: {self.product.dimension}\n\t" \
                f"Quantity: {self.quantity}"

