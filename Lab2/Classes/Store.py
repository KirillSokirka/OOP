from Classes.ItemModel import ItemModel


class Node:
    value = None
    right = None
    left = None


class Store:
    """
        Class that represents a store of products
        using binary tree. Data is sorted by products' id
        Public user interface -
            add_item - allows to add a new product
            delete_item - allows to delete a product
            show - shows all products
            get_product - find a concrete product by it id
            get_total_cost - return total price of all products
    """
    def __init__(self):
        self.__root = None

    def show(self):
        """
            help method,
            created for make using of this class easier
        :return: None
        """
        Store.__show(self.__root)

    @staticmethod
    def __show(node):
        if not node:
            return None
        Store.__show(node.left)
        print(f"Product:\n\t{node.value}")
        Store.__show(node.right)

    def add_item(self, item: ItemModel):
        if not isinstance(item, ItemModel):
            return TypeError
        new_node = Node()
        new_node.value = item
        if not self.__root:
            self.__root = new_node
            return None

        if not Store.__check_for_uniqueness(self.__root, item.product.Id):
            return None

        current_node = self.__root
        while True:
            if item.product.Id < current_node.value.product.Id:
                if current_node.left:
                    current_node = current_node.left
                    continue
                else:
                    current_node.left = new_node
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                    continue
                else:
                    current_node.right = new_node
                    break

    @staticmethod
    def __check_for_uniqueness(root: Node, id: int):
        """
            Method that checks if product is unique
        :param root: root of treee
        :param id: id of product
        :return: true if item is unique, false otherwise
        """
        if not root:
            return True
        if root.value.product.Id == id:
            root.value.quantity = root.value.quantity + 1
            return False
        if id < root.value.product.Id:
            return Store.__check_for_uniqueness(root.left, id)
        else:
            return Store.__check_for_uniqueness(root.right, id)

    def get_product(self, id):
        """
            Recursion function's wrapper
        :param id: if of product
        :return: Product in str
        """
        if not isinstance(id, int):
            raise TypeError
        if id < 0 or id > 100:
            raise ValueError
        return Store.__get_product(self.__root, id)

    @staticmethod
    def __get_product(root, id):
        if root.value.product.Id == id:
            return f"Product:\n\t{root.value}"
        if id < root.value.product.Id:
            return Store.__get_product(root.left, id)
        else:
            return Store.__get_product(root.right, id)

    def delete_item(self, id):
        if not isinstance(id, int):
            raise TypeError
        if not 0 < id < 100:
            raise ValueError
        self.__root = Store.__delete_item(self.__root, id)

    @staticmethod
    def __min_value_node(node):
        current = node
        while current.left:
            current = current.left
        return current

    @staticmethod
    def __delete_item(root: Node, id):
        if not root:
            return root
        if id < root.value.product.Id:
            root.left = Store.__delete_item(root.left, id)
        elif id > root.value.product.Id:
            root.right = Store.__delete_item(root.right, id)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp
            temp = Store.__min_value_node(root.right)
            root.value = temp.value
            root.right = Store.__delete_item(root.right, id)
        return root

    def get_total_cost(self):
        return Store.__get_total_cost(self.__root)

    @staticmethod
    def __get_total_cost(root):
        if not root:
            return 0
        return root.value.product.price * root.value.quantity + \
               Store.__get_total_cost(root.left) + Store.__get_total_cost(root.right)

