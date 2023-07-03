class DescriptorClass:
    def __get__(self, instance, owner):
        if instance is None:
            return f"{self.__class__.__name__}.{owner.__name__}"
        return f"value for {instance}"


class ClientClass:
    descriptor = DescriptorClass()

if __name__ == "__main__":
    client = ClientClass()
    print(client.descriptor)
    print(ClientClass.descriptor)
