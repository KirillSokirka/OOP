from json_files.json_worker import JSONWorker

class Pizza:

    def __init__(self, name, price, ingredients):
        self.name = name
        self.price = price
        self.ingredients = ingredients

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError
        if not value:
            raise ValueError
        self.__name = value

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        if not isinstance(value, int):
            raise TypeError
        if value <= 50:
            raise ValueError("Pizza less than 50 hrn isn't a pizza")
        self.__price = value

    @property
    def ingredients(self):
        return self.__ingredients

    @ingredients.setter
    def ingredients(self, value):
        if not isinstance(value, dict):
            raise ValueError
        if not all(isinstance(key, str) for key in value):
            raise TypeError("Ingredient must be a string")
        if not all(isinstance(value[key], int) for key in value):
            raise TypeError("A number of ingredients must be a int")
        self.__ingredients = value

    def add_ingredient(self, new_ingredient):
        if not isinstance(new_ingredient, dict):
            raise ValueError
        if not all(isinstance(key, str) for key in new_ingredient):
            raise TypeError("Ingredient must be a string")
        if not all(isinstance(new_ingredient[key], int) for key in new_ingredient):
            raise TypeError("A number of ingredients must be a int")
        for key in new_ingredient:
            if self.__ingredients.get(key):
                self.__ingredients[key] += new_ingredient[key]
            else:
                self.__ingredients[key] = new_ingredient[key]

    def __str__(self):
        return f'Pizza:\n\t' \
               f'name - {self.__name}\n\t' \
               f'price - {self.__price}\n\t' \
               f'ingredients: {self.__ingredients}'

    def __dict__(self):
        return {
            'name' : self.__name,
            'price' : self.__price,
            'ingredients' : self.__ingredients
        }