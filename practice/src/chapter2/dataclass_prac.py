from typing import List
from dataclasses import dataclass, field

# define size
R = 26

@dataclass
class RtrieNode:
    size = R
    value: int
    next_: List["RtrieNode"] = field(default_factory=lambda: [None] * R)

    def __post_init__(self):
        if len(self.next_) != len(self.size):
            raise ValueError('next_ length is not correct!')
        


@dataclass
class Person:
    name: str
    age: int
    email: str = field(default="hyunwoo@gmail.com")

if __name__ == "__main__":
    p = Person("Alice", 30)
    print(p.email)