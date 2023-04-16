from dataclasses import dataclass

USERS = [
    (i, f"first_name_{i}", f"last_name_{i}") for i in range(1_000)
]

@dataclass
class User:
    user_id: int
    first_name: str
    last_name: str

def bad_users_from_rows(dbrows) -> list:
    "Read DB record and then make the User from DB record"
    return [User(row[0], row[1], row[2]) for row in dbrows]

def user_from_rows(dbrows) -> list:
    return [
        User(user_id, first_name, last_name) for (user_id, first_name, last_name) in dbrows
        # or use this!!
        # User(*row) for row in dbrows
    ]
