# BaseTokenizer class with UppercaseMixin mixed in
class BaseTokenizer:
    def __init__(self, str_token):
        self._str_token = str_token

    def __iter__(self):
        yield from self._str_token.split("-")

# Mixin class for uppercase functionality
class UpperIterableMixin(BaseTokenizer):
    def __iter__(self):
        return map(str.upper, super().__iter__())
    
class tokenizer(UpperIterableMixin, BaseTokenizer):
    '''mixin tokenizer'''
    pass


if __name__ == "__main__":
    # Create an instance of BaseTokenizer with a string
    tk = BaseTokenizer("hello-world-python")
    tk2 = UpperIterableMixin("hello-world-python")

    mixin_tk = tokenizer("hello-world-python")



    # Iterate over the tokenizer and print the values
    for token in tk:
        print(token)

    for token in tk2:
        print(token)
    
    for token in mixin_tk:
        print(token)

    print([cls.__name__ for cls in tokenizer.mro()])