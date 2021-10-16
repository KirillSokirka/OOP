import string


class Product:

    __list_id = []

    def __init__(self, id, name, description, price, dimension):
        self.name = name
        self.description = description
        self.price = price
        self.dimension = dimension
        if not isinstance(id, int):
            raise TypeError
        if id in Product.__list_id:
            raise ValueError
        Product.__list_id.append(id)
        self.Id = id

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__name = value

    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, value):
        if not isinstance(value, str):
            raise TypeError
        self.__description = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value <= 0:
            raise ValueError
        self.__price = value

    @property
    def dimension(self):
        return self.__quantity

    @dimension.setter
    def dimension(self, value):
        if isinstance(value, str):
            if not value:
                raise ValueError
        self.__quantity = value

    def __str__(self):
        return f"{self.name}|{self.description}|Price - {self.price}|Quantity - {self.dimension}"

