from functools import wraps
from typing import Sequence, Optional

from log import logger


_DEFAULT_RETRIES_LIMIT = 3


class ControlledException(Exception):
    """A generic exception on the program's domain."""

class WithRetry:
    def __init__(
            self,
            retries_limit: int = _DEFAULT_RETRIES_LIMIT,
            allowed_exceptions: Optional[Sequence[Exception]] = None
        ) -> None:

        self.retries_limit = retries_limit
        self.allowed_exceptions = allowed_exceptions or (ControlledException, )

    def __call__(self, operation):
        @wraps(operation)
        def wrapped(*args, **kwargs):
            last_raised = None

            for _ in range(self.retries_limit):
                try:
                    return operation(*args, **kwargs)
                except self.allowed_exceptions as e:                    
                    print(f"retry {operation.__qualname__}, caused by{e}")
                    last_raised = e
            raise last_raised
        return wrapped

if __name__ == "__main__":
    def task():
        print(5/0)

    @WithRetry(retries_limit=5)
    def run_with_custom(task):
        return task

    run_with_custom(task)