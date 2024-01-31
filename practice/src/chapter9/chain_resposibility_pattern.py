import re
from typing import Optional, Pattern

class Event:
    pattern: Optional[Pattern[str]] = None

    def __init__(self, next_event=None):
        self.successor = next_event
    
    def process(self, logline: str):
        if self.can_process(logline):
            return self._process(logline)
        
        if self.successor is not None:
            return self.successor.process(logline)
        
    def _process(self, logline: str) -> dict:
        parsed_data = self._parse_data(logline)
        return {
            "type": self.__class__.__name__,
            "id": parsed_data["id"],
            "value": parsed_data["value"]
        }
    
    @classmethod
    def can_process(cls, logline: str) -> bool:
        return (
            cls.pattern is not None and cls.pattern.match(logline) is not None
        )
    
    @classmethod
    def _parse_data(cls, logline: str) -> dict:
        if not cls.pattern: # 정규표현식이 없으면
            return {} 
        if (parsed:= cls.pattern.match(logline)) is not None:
            return parsed.groupdict()
        return {}
    
class LoginEvent(Event):
    pattern = re.compile(r"regex")

class LogoutEvnet(Event):
    patter = re.compile(r"regex")