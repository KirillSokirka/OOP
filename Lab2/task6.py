from Classes.Product import Product
from Classes.ItemModel import ItemModel
from Classes.Store import Store


def main():
    prod1 = Product(1, "Prod1", "Desc1", 100, 1)
    prod2 = Product(2, "Prod2", "Desc2", 200, 2)
    prod3 = Product(3, "Prod3", "Desc3", 100, 3)
    prod5 = Product(5, "Prod5", "Desc5", 100, 5)
    store = Store()
    store.add_item(ItemModel(prod2, 2))
    store.add_item(ItemModel(prod3, 1))
    store.add_item(ItemModel(prod1, 1))
    store.add_item(ItemModel(prod5, 1))
    store.delete_item(3)
    store.show()


main()
