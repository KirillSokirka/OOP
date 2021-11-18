from Pizzeria import Pizzeria
from models.Pizza import Pizza
from models.PizzaOfTheDay import PizzaOfTheDay
from json_worker import JSONWorker


pizzeria = Pizzeria('BrothersPizza')
pizza = pizzeria.get_pizza_of_the_day(1)
pizza.add_ingredient({'chicken' : 2, 'hot sauce': 2})
if pizzeria.order_pizza(pizza):
    print(f'Making for u {pizza}')

plain_pizza = Pizza('Cool pizza', 150, {'peperony' : 2, 'cheese':3, 'plain sauce':1})
pizzeria.add_your_custom_pizza(plain_pizza)

menu = pizzeria.standart_menu()
print('Menu:')
for p in menu:
    print(p)

pizza = pizzeria.get_standart_pizza('Cool pizza')
pizza.add_ingredient({'becon':1})
if pizzeria.order_pizza(pizza):
    print(f'Making for u {pizza}')