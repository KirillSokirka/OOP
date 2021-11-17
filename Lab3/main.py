from models.Pizza import Pizza
from models.PizzaOfTheDay import PizzaOfTheDay
from json_files.json_worker import JSONWorker


pizza = PizzaOfTheDay.get_pizza_of_the_day(2)
print(pizza)
pizza.add_ingredient({'chicken' : 2, 'hot sauce': 2})
print(pizza)

plain_pizza = Pizza('Custom', 150, {'peperony' : 2, 'cheese':3, 'plain sauce':1})
JSONWorker.save_to_json('json_files/pizza.json', plain_pizza)

temp = JSONWorker.get_object_by_key('json_files/pizza.json', 'name', 'Custom')
plain_pizza = Pizza(**temp)
print(plain_pizza)
