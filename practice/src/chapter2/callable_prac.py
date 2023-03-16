def greet(name):
    print(f"Hello, {name}!")
    return

class Greeter:
    def __init__(self, name):
        self.name = name

    def __call__(self):
        print(f"Hello, {self.name}!")
        return
    
from collections import defaultdict
class CallCount:
    def __init__(self):
        self._count_dict = defaultdict(lambda: 0)
    
    def __call__(self, argument):
        self._count_dict[argument] += 1
        return self._count_dict



if __name__ == "__main__":
    g = Greeter("srBae")
    print(greet("hyunwoo"))
    print(g())


    cc = CallCount()
    cc(1)
    cc(2)
    cc(1)
    if callable(cc):
        print('cc is callable!')
        print(cc._count_dict)
