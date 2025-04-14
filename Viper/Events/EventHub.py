from .EventHandler import EventHandler

class EventHub:
    def __init__(self):
        self._incoming_messages_event_handler = EventHandler()

    @property
    def incoming_messages_event_handler(self):
        return self._incoming_messages_event_handler
        
