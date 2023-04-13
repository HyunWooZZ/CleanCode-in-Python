class BaseModule:
    module_name = "top"

    def __init__(self, module_name):
        self.name = module_name

    def __str__(self):
        return f"{self.module_name}: {self.name}"
    
class BaseModule2(BaseModule):
    module_name = "module-2"

class BaseModule3(BaseModule):
    module_name = "module-3"

class BaseModule4(BaseModule):
    module_name = "module-4"

class compose_moduleA(BaseModule2, BaseModule3):
    """composed module"""

class compose_moduleB(BaseModule3, BaseModule4):
    """composed module"""

if __name__ == "__main__":
    ## In python using the MRO algoritm, python solve class conflict problem..
    # below case what is the module name????? 
    # module-2? module-3? run this!!!!  
    print(str(compose_moduleA("hyunwoo")))

    ## if you want to know the decision order.. run this!
    # you can know the class hierachy!!!!
    print([cls.__name__ for cls in compose_moduleA.mro()])