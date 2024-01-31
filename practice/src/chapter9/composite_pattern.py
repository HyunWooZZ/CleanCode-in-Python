# 순환 종속성: ProductBundle 클래스를 정의할 때, ProductBundle 타입 자체가 아직 완전히 정의되지 않았습니다. 파이썬에서 자신의 정의 내에서 클래스를 참조할 때, 클래스가 완전히 정의되지 않았다면 문자열 리터럴(예: "ProductBundle")을 사용하여 참조해야 합니다. 이는 파이썬에 "이 이름은 나중에 정의될 것이므로, 클래스의 이름으로 처리하라"고 알려줍니다. 특히 두 클래스가 서로를 참조하는 상황에서 중요합니다.

# 지연된 평가: 문자열 리터럴을 사용하면 파이썬이 타입의 평가를 연기할 수 있습니다. 스크립트 전체가 처리되면 파이썬은 "ProductBundle"이 ProductBundle 클래스를 참조한다는 것을 이해합니다. 이 접근 방식은 클래스 정의의 순서와 관련된 문제를 피하는 데 도움이 됩니다.


from typing import Iterable, Union

class Product:
    def __init__(self, name: str, price: float) -> None:
        self._name = name
        self._price = price
    
    @property
    def price(self) -> float:
        return self._price
    
class ProductBundle:
    def __init__(
        self,
        name: str,
        perc_discount: float,
        *products: Iterable[Union[Product, "ProductBundle"]]
    ) -> None:
        self._name = name
        self._perc_discount = perc_discount
        self._products = products
    
    @property
    def price(self) -> float:
        total = sum(p.price for p in self._products)
        return total * (1 - self._perc_discount)