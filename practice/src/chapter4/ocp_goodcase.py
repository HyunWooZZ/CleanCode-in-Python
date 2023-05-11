class Event:
    def __init__(self, raw_data):
        self._raw_data = raw_data
    
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return False
    
class UnknownEvent(Event):
    """Event which can handle with just data.."""

class LoginEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return (
            event_data["before"]["session"] == 0
            and event_data["after"]["session"] == 1
        )
    
class LogoutEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict) -> bool:
        return(
            event_data["before"]["session"] == 1
            and event_data["after"]["session"] == 0
        )
class transactionEvent(Event):
    @staticmethod
    def meets_condition(event_data: dict):
        return event_data["after"].get("transaction") is not None

class SystemMonitor(Event):
    """Categorizing the event which made by system"""

    def __init__(self, event_data):
        self._event_data = event_data
    
    def identify_event(self):
        """
        fuction that return the detail event
        we should note that the Event.__subclasses__() method!!! 
        if we use this method the identify_event method is closed..
        but the event is opened for expand!!!!
        """
        for event_cls in Event.__subclasses__():
            try:
                if event_cls.meets_condition(self._event_data):
                    return event_cls(self._event_data)
            except KeyError:
                continue
        return UnknownEvent(self._event_data)

if __name__ == "__main__":
    l1 = SystemMonitor({"before": {"session": 0}, "after": {"session": 1}})
    print(l1.identify_event().__class__.__name__)

    l2 = SystemMonitor({"before": {"session": 1}, "after": {"session": 0}})
    print(l2.identify_event().__class__.__name__)

    l3 = SystemMonitor({"before": {"session": 1}, "after": {"session": 1}})
    print(l3.identify_event().__class__.__name__)

    l4 = SystemMonitor({"before": {"session": 1}, "after": {"transaction": 'tran1'}})
    print(l4.identify_event().__class__.__name__)