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

if __name__ == "__main__":
    # Create an instance of BaseTokenizer with a string
    tokenizer = BaseTokenizer("hello-world-python")
    tokenizer2 = UpperIterableMixin("hello-world-python")

    # Iterate over the tokenizer and print the values
    for token in tokenizer:
        print(token)

    for token in tokenizer2:
        print(token)