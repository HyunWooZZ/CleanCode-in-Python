from dataclasses import dataclass

def _resolver_method(self, attr):
    if attr.startswith('resolve_'):
        *_, actual_attr = attr.partition('resolve_')
    else:
        actual_attr = attr
    try:
        return self.__dict__[actual_attr]
    except KeyError as e:
        raise AttributeError from e
    
def with_resolver(cls):
    """define the User defined decision method assign to __getattr__"""
    cls.__getattr__ = _resolver_method
    return cls

@dataclass
@with_resolver
class Customer:
    customer: str
    name: str
    address: str

if __name__ == "__main__":
    hyunwoo = Customer('VIP', 'hyunwoo', 'pan_gyo_ro')
    print(hyunwoo.resolve_customer)