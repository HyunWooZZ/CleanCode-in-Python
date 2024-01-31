from typing import Iterable, Dict, Callable

class DictQuery:
    def __init__(self, **kwargs):
        self._raw_query = kwargs

    def render(self) -> dict:
        return self._raw_query

class QueryEnhancer:
    def __init__(self, query: DictQuery):
        self.decorated = query

    def render(self):
        return self.decorated.render()

class RemoveEmty(QueryEnhancer):
    def render(self):
        original = super().render()
        return {k: v.lower() for k, v in original.items() if v}

class CaseInsensitive(QueryEnhancer):
    def render(self):
        original = super().render()
        return {k: v.lower() for k, v in original.items()}
    
### another decorator pattern ###

class QueryEnhancer:
    def __init__(self,
        query: DictQuery,
        *decorators: Iterable[Callable[[Dict[str, str]], Dict[str, str]]]
        ) -> None:
        self._decorated = query
        self._decorators = decorators
    
    def render(self):
        current_result = self._decorated.render()
        for deco in self._decorators:
            current_result = deco(current_result)
        return current_result