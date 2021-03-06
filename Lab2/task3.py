from Classes.Product import Product
from Classes.Customer import Customer
from Classes.Order import Order


def main():
    Petya = Customer("Petya", "Pupkin", "+380(50)-180-34-34", 10)
    #prod1 = Product(1,"Prod1", "Desc1", 200, 3)
    prod2 = Product(2,"Prod2", "Desc2", 300, 1)
    prod3 = Product(3 ,"Prod3", "Desc3", 100, 6)
    order_product = {}
    order_product[prod2] = 1
    order_product[prod3] = 1
    order = Order(Petya, order_product)
    print(order.products)
    order.add_product({Product(4, "Prod4", "Desc4", 240, 1): 1})
    print(order.products)
    order.del_product(2)
    print(order.products)
    print(f'Total value {order.total_value} hrn')
    print(f'Can Petya afford it? {order.check_if_affordable()}')


main()
