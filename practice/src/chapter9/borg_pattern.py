class BaseFetcher:
    def __init__(self, source):
        self.source = source

class TagFetcher(BaseFetcher):
    _attributes = {}

    def __init__(self, source):
        self.__dict__ = self.__class__._attributes
        super().__init__(source)


class BranchFetcher(BaseFetcher):
    _attributes = {}

    def __init__(self, source):
        self.__dict__ = self.__class__._attributes
        super().__init__(source)

tag = TagFetcher('hello!')
print(tag.__dict__)
branch1 = BranchFetcher('hello!!')
print(branch1.__dict__)

branch2 = BranchFetcher('world!!')
print(branch1.__dict__)
print(branch2.__dict__)

branch2._attributes['tag'] = 1

print(branch2.__dict__)
print(branch1.__dict__)


class TagFetcher2(BaseFetcher):
    _attributes = {"name" : "HYUNWOO"}

    def __init__(self, source):
        super().__init__(source)

tag2 = TagFetcher2('test')

print(TagFetcher2.__mro__)