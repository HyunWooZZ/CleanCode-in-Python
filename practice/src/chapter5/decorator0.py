def add_numbers(a, b):
    return a + b

def wrap(func):
    def wrapper(*args, **kwargs):
        print(f"Calling function {func.__name__} with args: {args}, kwargs: {kwargs}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} returned: {result}")
        return result
    return wrapper

wrapped_add_numbers = wrap(add_numbers)

result = wrapped_add_numbers(3, 5)
print(result)



from functools import wraps
def my_decorator(f):
    @wraps(f)
    def wrapper(*args, **kwds):
        print('Calling decorated function')
        return f(*args, **kwds)
    return wrapper

@my_decorator
def example():
    """Docstring"""
    print('Called example function')

example()

print(example.__name__)

print(example.__doc__)


## currying ## 
# ### scala code ###
# def add(a: Int)(b: Int): Int = a + b

# // Curried function
# val add5: Int => Int = add(5)

# // Calling the curried function
# val result = add5(3)
# println(result)  // Output: 8

#### equal with python code ###
from functools import partial

def add(a, b):
    return a + b

# Partial function application using functools.partial()
add5 = partial(add, 5)

# Calling the partially applied function
result = add5(3)
print(result)  # Output: 8