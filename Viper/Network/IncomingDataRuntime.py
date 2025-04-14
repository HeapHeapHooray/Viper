import threading
from .SimulatorConnectionHandler import SimulatorConnectionHandler
from Packet import PacketFactory

class IncomingDataRuntime:
    def __init__(self,connection_handler: SimulatorConnectionHandler):
        self._connection_handler = connection_handler
        self._receive_data_thread = threading.Thread(target=self._receive_data)
        self._running = False
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
            print(PacketFactory.create_from_bytes(self._connection_handler.receive_data()[0]).message.convert_to_string())
        
