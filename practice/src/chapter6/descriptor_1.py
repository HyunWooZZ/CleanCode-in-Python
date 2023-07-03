from typing import Callable, Any

class Validation:
    def __init__(
            self, validation_fuction: Callable[[Any], bool], error_msg: str
    ) -> None:
        self.validation_fuction = validation_fuction
        self.error_msg = error_msg

    def __call__(self, value):
        if not self.validation_fuction(value):
            raise ValueError(f"{value!r} {self.error_msg}")
        
class Field:
    def __init__(self, *validations):
        self._name = None
        self.validations = validations

    def __set_name__(self, owner, name):
        self._name = name
    
    def __get__(self, instance, owner):
        if instance is None:
            return owner
        return instance.__dict__[self._name]
    
    def validate(self, value):
        for validation in self.validations:
            validation(value)

    def __set__(self, instance, value):
        self.validate(value)
        instance.__dict__[self._name] = value


class ClientClass:
    descriptor = Field(
        Validation(lambda x: isinstance(x, (int, float)), "is not the numbers"),
        Validation(lambda x: x >= 0, "is lowwer than 0")
    )

if __name__ == "__main__":
    client = ClientClass()
    client.descriptor = 42
    print(f"client`s value is {client.descriptor}")

    print("set the minus value")
    client.descriptor = -42

    