import threading
from .SimulatorConnectionHandler import SimulatorConnectionHandler
from Packet import PacketFactory
from Events import EventHub

def print_message(message):
    print(message.convert_to_string())

class IncomingDataRuntime:
    def __init__(self,connection_handler: SimulatorConnectionHandler,event_hub: EventHub):
        self._connection_handler = connection_handler
        self._event_hub = event_hub
        self._receive_data_thread = threading.Thread(target=self._receive_data)
        self._running = False
        self._event_hub.incoming_messages_event_handler.register_callback("ObjectUpdate",print_message)
    def start(self):
        self._running = True
        self._receive_data_thread.start()
    def stop(self):
        self._running = False
        self._receive_data_thread.stop()
    def is_running(self):
        return self._running
    def _receive_data(self):
        while self._running:
            #print(self._connection_handler.receive_data())
            message = PacketFactory.create_from_bytes(self._connection_handler.receive_data()[0]).message
            self._event_hub.incoming_messages_event_handler.trigger(type(message).__name__,message)
