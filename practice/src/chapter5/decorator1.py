from datetime import datetime
from dataclasses import dataclass
import unittest
import sys

def hide_field(field) -> str:
    return '**redacted**'

def format_time(field_timestamp: datetime) -> str:
    return field_timestamp.strftime("%Y-%m-%d %H:%M")

def show_original(event_field):
    return event_field

class EventSerializer:
    def __init__(self, serialization_field: dict) -> None:
        self.serialization_field = serialization_field

    def serialize(self, event) -> dict:
        return {
            field: transformation(getattr(event, field))
            for field, transformation in self.serialization_field.items()
        }
    
class Serialization:
    def __init__(self, **transformations):
        self.serializer = EventSerializer(transformations)

    def __call__(self, event_class):
        def serialize_method(event_instance):
            return self.serializer.serialize(event_instance)
        
        event_class.serialize = serialize_method
        return event_class
    
@Serialization(
    username=str.lower,
    password=hide_field,
    ip=show_original,
    timestamp=format_time
)
@dataclass
class LoginEvent:
    username: str
    password: str
    ip: str
    timestamp: datetime

class TestLoginEventSerialized(unittest.TestCase):
    @unittest.skipIf(
        sys.version_info[:3] < (3, 7, 0), reason="Requires Python 3.7+ to run"
    )
    def test_serializetion(self):
        event = LoginEvent(
            "username", "password", "127.0.0.1", datetime(2016, 7, 20, 15, 45)
        )
        expected = {
            "username": "username",
            "password": "**redacted**",
            "ip": "127.0.0.1",
            "timestamp": "2016-07-20 15:45",
        }
        self.assertEqual(event.serialize(), expected)


if __name__ == "__main__":
    unittest.main()

    # my_little_event = LoginEvent("username", "password", "127.0.0.1", datetime(2016, 7, 20, 15, 45))
    # print(dir(my_little_event))


### dataclass instance is created => init serializing
### => wrapped the dataclass => ins_data = ins_serial(ins_data) => add serialize method..!!!