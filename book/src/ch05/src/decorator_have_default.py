from functools import wraps

DEFAULT_X = 3
DEFAULT_Y = 4

def decorator(function=None, *, x=DEFAULT_X, y=DEFAULT_Y):
    if function is None:
        # when they call the decorator like this @decorator(....)
        def decorated(function):
            @wraps(function)
            def wrapped():
                return function(x, y)
            return wrapped
        return decorated
    
    else:
        @wraps(function)
        def wrapped():
            return function(x, y)
        return wrapped
    
from functools import partial

def decorator_sec(function=None, *, x=DEFAULT_X, y=DEFAULT_Y):
    if function is None:
        return partial(decorator_sec, x=x, y=y)
        
        
    
    @wraps(function)
    def wrapped():
        print(function)
        return function(x, y)
    
    return wrapped

@decorator_sec(x = 5, y = 11)
def sum_of_mine(x, y):
    return x + y

print(sum_of_mine())
