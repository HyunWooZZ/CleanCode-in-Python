class DynamicAttributes:
    def __init__(self, attribute):
        self.attribute = attribute

    # Here you can dynamically generate the attribute or proxy attribute access to another object
    # If you don't handle the attribute here, an AttributeError will be raised
    def __getattr__(self, attr):
        if attr.startswith("fallback_"):
            name = attr.replace('fallback_', "")
            return f"[fallback resolved] {name}"
        raise AttributeError(f"There`s no {attr} property...")
    
if __name__ == "__main__":
    da = DynamicAttributes('value')
    print(da.attribute)

    print(da.fallback_test)

    print(getattr(da, 'new_thing', 'default'))
    


    