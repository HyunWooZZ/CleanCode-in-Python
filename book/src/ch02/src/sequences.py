"""Clean Code in Python - Chapter 2: Pythonic Code

> Sequences
"""
from collections.abc import Sequence


class Items(Sequence):
    def __init__(self, *values):
        self._values = list(values)

    def __len__(self):
       return len(self._values)

    def __getitem__(self, item):
        return self._values.__getitem__(item)
    
if __name__ == '__main__':
    items = Items('apple', 'pear')
    help(len)
    print(items[1])    

