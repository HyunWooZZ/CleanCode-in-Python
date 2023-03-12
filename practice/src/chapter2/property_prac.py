class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def area(self):
        return self._width * self._height
    
    @property
    def perimeter(self):
        return 2 * (self._width + self._height)
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError(f"Width should be positive, we got {value}")
        self._width = value
    
    @property
    def height(self):
        return self._height
    
    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError(f"height should be positive, we got {value}")
        self._height = value

if __name__ == "__main__":
    my_rectangle = Rectangle(10, 5)
    print(f"rectangle area is {my_rectangle.area}")
    
    print(f"rectangle`s height is {my_rectangle.height} and width is {my_rectangle.width}")

    my_rectangle.height = 1

    print(f"I don`t like too tall rectangle so changed... my rectangle`s height is {my_rectangle.height} and width is {my_rectangle.width}")

    my_rectangle.height = -1