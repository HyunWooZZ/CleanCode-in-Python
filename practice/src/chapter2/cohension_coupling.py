# Bad example - low cohesion, tight coupling

# In this example, 
# the Calculator class is responsible for performing arithmetic operations,
# but it is also responsible for keeping track of the current total. 
# The CalculatorUI class is responsible for displaying the calculator interface and handling button clicks,
# but it is tightly coupled to the Calculator class - it creates a new instance of the Calculator class and calls its methods directly.


class Calculator:
    def __init__(self):
        self.total = 0

    def add(self, num):
        self.total += num

    def subtract(self, num):
        self.total -= num

class CalculatorUI:
    def __init__(self):
        self.calculator = Calculator()

    def display_total(self):
        print(self.calculator.total)

    def add_button_clicked(self, num):
        self.calculator.add(num)
        self.display_total()

    def subtract_button_clicked(self, num):
        self.calculator.subtract(num)
        self.display_total()

# Good example - high cohesion, loose coupling

# In this example, the Calculator class is responsible only for performing arithmetic operations,
# and the CalculatorUI class is responsible only for displaying the interface and handling user input.
# The two classes are loosely coupled - the CalculatorUI class takes a Calculator object as a parameter,
# rather than creating a new instance itself,
# and the two classes communicate through a well-defined interface (the button_clicked method). 
# This design allows the two classes to be modified independently 
# and makes the system easier to maintain and extend.

class Calculator:
    def add(self, num1, num2):
        return num1 + num2

    def subtract(self, num1, num2):
        return num1 - num2

class CalculatorUI:
    def __init__(self, calculator):
        self.calculator = calculator

    def display_result(self, result):
        print(result)

    def button_clicked(self, operation, num1, num2):
        if operation == "add":
            result = self.calculator.add(num1, num2)
        elif operation == "subtract":
            result = self.calculator.subtract(num1, num2)
        self.display_result(result)

