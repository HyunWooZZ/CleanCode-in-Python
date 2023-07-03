from logging import Logger

class DescriptorWithName:
    def __init__(self, name):
        self.name = name
    
    def __get__(self, instance, value):
        if instance is None:
            return self
        Logger.info(msg=f"Getting a {value} from {instance}")
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        instance.__dict__[self.name] = value

class ClientClass:
    descriptor = DescriptorWithName("descriptor")

if __name__ == '__main__':
    client = ClientClass()
    client.descriptor = "value"
    print(client.descriptor)
