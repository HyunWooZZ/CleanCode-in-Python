from collections.abc import *

## inherit directly..
## So we just implement @abstract method!  
class C(Sequence):
    def __init__(self):
        ...
    def __getitem__(self, index):
        ...
    def __len__(self):
        ...
    def count(self):
        ...

## if we did not inherit Sequence, below class how can be subclass Sequence?
## Just use register!
class D:
    def __init__(self):
        ...
    def __getitem__(self, index):
        ...
    def ___len__(self):
        ...
    def count(self, value):
        ...
    def index(self, value):
        ...


class ListBasedSet(Set):
    '''
    Alternatable SET using list, favoring space over speed
    and not requiring the set elements to be hashable.
    '''
    def __init__(self, iterable):
        self.elements = lst = []
        for value in iterable:
            if value not in lst:
                lst.append(value)

    def __iter__(self):
        return iter(self.elements)
    
    def __contains__(self, value):
        return value in self.elements
    
    def __len__(self):
        return len(self.elements)
    

    
            



if __name__ == "__main__":
    temp = C()
    print('###inherit###')
    print(issubclass(C, Sequence))
    print(isinstance(temp, Sequence))
    print('##################')
    
    print('### not inherit ###')
    Sequence.register(D)
    print(issubclass(D, Sequence))
    
    print('### example ###')
    s1 = ListBasedSet('abcdef')
    s2 = ListBasedSet('defghi')
    overlap = s1 & s2

    ## using iterable magic method
    for i in overlap:
        print(i)

    ## using contain magic method
    print('d' in overlap)

    ## using len magic method
    print(len(overlap))

