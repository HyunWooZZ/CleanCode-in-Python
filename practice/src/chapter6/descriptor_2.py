class ProtectAttribute:
    def __init__(self, requires_role=None) -> None:
        self.permission_required = requires_role
        self._name = None

    def __set_name__(self, owner, name):
        self._name = name

    def __set__(self, user, value):
        if value is None:
            raise ValueError(f"we can`t set {self._name} to None")
        user.__dict__[self._name] = value

    def __delete__(self, user):
        if self.permission_required in user.permissions:
            user.__dict__[self._name] = None
        else:
            raise ValueError(
                f"{user!s} user doesn`t have {self.permission_required} permission"
            )

class User:
    """Having a admin permission User can delete email."""
    email = ProtectAttribute(requires_role='admin')
    
    def __init__(self, username: str, email: str, permission_list: list = None) -> None:
        self.username = username
        self.email = email
        self.permissions = permission_list or []

    def __str__(self):
        return self.username
