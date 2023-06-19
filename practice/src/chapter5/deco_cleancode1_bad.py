from dataclasses import dataclass

class BaseResolverMixin:
    def __getattr__(self, attr: str):
        if attr.startswith('resolve_'):
            *_, actual_attr = attr.partition('resolve_')
        else:
            actual_attr = attr
        try:
            return self.__dict__[actual_attr]
        except KeyError as e:
            raise AttributeError from e
        
@dataclass
class Customer(BaseResolverMixin):
    customer_id: str
    name: str
    address: str

if __name__ == "__main__":
    hyunwoo = Customer('1414', 'hyunwoo', 'pan_gyo')
    print(hyunwoo.resolve_address)
