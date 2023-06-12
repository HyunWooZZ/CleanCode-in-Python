import inspect
from functools import wraps
from time import time

def timing(callable):
    @wraps(callable)
    def wrapped(*args, **kwargs):
        start = time()
        result = callable(*args, **kwargs)
        latency = time() - start
        return {"latency": latency, "result": result}
    
    @wraps(callable)
    async def wrapped_coro(*args, **kwargs):
        start = time()
        result = await callable(*args, **kwargs)
        latency = time() - start
        return {"latency": latency, "result": result}
    
    if inspect.iscoroutinefunction(callable):
        return wrapped_coro
    
    return wrapped

