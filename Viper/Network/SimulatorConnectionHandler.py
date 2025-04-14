from .UDPSocket import UDPSocket
from .MessageSender import MessageSender
from typing import Tuple
from Message import Message

class SimulatorConnectionHandler:
    def __init__(self,simulator_ip: str,simulator_port: int):
        self._udp_socket = UDPSocket(simulator_ip,simulator_port,8096)
        self._message_sender = MessageSender(self._udp_socket)
    def send_message(self,message: Message):
        self._message_sender.send_message(message)
    def receive_data(self) -> Tuple[bytes,str]:
        return self._udp_socket.receive_data()
