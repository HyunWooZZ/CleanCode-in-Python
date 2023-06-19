# decorator good case #
# 1. papameter transform
# 2. code tracing
# 3. validating the parameter
# 4. retry logic
# 5. simplify some repeated task class.

class DomainObject:
    """my name is hyunwoo"""
    def __init__(self, *args):
        pass

    def process(self):
        """hello my docs"""
        print("hello")

####### function signiture change ######


from functools import wraps

def DomainArgs(object):
    @wraps(object)
    def wrapped(*args, **kwargs):
        temp_ins = object(*args, **kwargs)
        return temp_ins
    return wrapped


@DomainArgs
def resolver(helper):
    """origin docs"""
    helper.process()

print(resolver(DomainObject(1, 2, 3)).__name__)