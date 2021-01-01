import socket
from typing import Tuple
import collections

ConnectedTo = collections.namedtuple("ConnectedTo",["ip","port"])

class UDPSocket:
    def __init__(self,connect_to_ip: str,connect_to_port: int,receive_data_buffer_size: int):
        self._receive_data_buffer_size = receive_data_buffer_size
        self._socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        self._connected_to_ip = connect_to_ip
        self._connected_to_port = connect_to_port
        self._socket.connect((connect_to_ip,connect_to_port))
    def get_connected_to_ip_and_port(self):
        return ConnectedTo(self._connected_to_ip,self._connected_to_port)
    def send_data(self,data: bytes):
        self._socket.sendto(data,(self._connected_to_ip,self._connected_to_port))
    def receive_data(self) -> Tuple[bytes,str]:
        return self._socket.recvfrom(self._receive_data_buffer_size)
        
        
