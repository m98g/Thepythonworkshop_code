class Polygon():
    # This is the doc string it is printed when the user wants to print
    # Polygon.__doc__
    """
    This object defines a shape.
    """
    # This is the init function and it takes the side lengths as a list of 
    # values from the child class Rectangle
    def __init__(self, side_lengths):
        self.side_lengths = side_lengths
    # The __str__ is what is printed to the consol when the user calls the 
    # class as a string.
    def __str__(self):
        return f'Polygon with {num_sides} sides'
    #This is called with square.num_sides. It is easier this way than to hard
    # code an attribute. This solution is dynamic but callabel like an class 
    # attribute.
    @property
    def num_sides(self):
        return len(self.side_lengths)
    #This is called with square.perimeter. It is easier this way than to hard
    # code an attribute. This solution is dynamic but callabel like an class 
    # attribute.
    @property
    def perimeter(self):
        return sum(self.side_lengths)

class Rectangle(Polygon):
    # When the user calls the class and the two parameteters are defined the class
    # repeates them and puts them into a list of values for the parents class
    # to understand what is needed. The super method ensures that the parameter
    # can be manipulated.
    def __init__(self, height, width):
        # Here __init__ is only there to reference the called method of the
        # parent class. It could also, in another use case, be either of the 
        # two propteries num_sides or perimeter or any other mehtod defined in
        # the parent class. The mehtod is defined after "super()." and the 
        # positional arguemnts follow in the parentheses.
        super().__init__([height, width, height, width])
    # callable property of the class rectangle which computes the area of the 
    # shape.
    @property
    def area(self):
        return self.side_lengths[0] * self.side_lengths[1]

class Square(Rectangle):
    # Used to only take one positional argument and then split it for the two
    # parent classes to understand.
    def __init__(self, height):
        super().__init__(height, height)


rectangle = Rectangle(1, 5)

print(rectangle.area)

print(rectangle.perimeter)

square = Square(2)

print(square.area)
print(square.perimeter)

print(Polygon.__doc__)