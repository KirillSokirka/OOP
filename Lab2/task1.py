
class Rectangle:
    """

    """

    def __init__(self, height=1, width=1):
        if not isinstance(height, float) or not isinstance(width, float):
            raise TypeError("Invalid type")
        if not 0.0 <= height <= 20.0 or not 0.0 <= width <= 20.0:
            raise ValueError("Invalid range")
        self.height = height
        self.__width = width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if not isinstance(height, float):
            raise Exception("Invalid type")
        if not 0.0 <= height <= 20.0:
            raise Exception("Invalid range")
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        if not isinstance(width, float):
            raise Exception("Invalid type")
        if not 0.0 <= width <= 20.0:
            raise Exception("Invalid range")
        self.__width = width

    def calculate_square(self):
        return self.height * self.width

    def calculate_area(self):
        return 2 * (self.height + self.width)


def main():
    try:
        rect1 = Rectangle()
        rect1.height = 5.5
        rect1.width = "1"
        print("Rectangle width ->", rect1.width, "\nRectangle height -> ", rect1.height)
        print("Square:", rect1.calculate_square())
        print("Area:", rect1.calculate_area())
    except Exception as e:
        print(e)


main()