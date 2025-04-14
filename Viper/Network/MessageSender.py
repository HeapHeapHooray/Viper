from Packet.PacketHeaderFlags import PacketHeaderFlags
from Packet.PacketHeader import PacketHeader
from Packet.Packet import Packet

class MessageSender:
    def __init__(self,socket):
        self._socket = socket
        self.sequence_number = 0
    def send_message(self,message):
        header_flags = PacketHeaderFlags(False,False,False,False)
        header = PacketHeader(header_flags,self.sequence_number,b'')
        packet = Packet(header,message)

        print("Packet:",packet.convert_to_string())

        self._socket.send_data(packet.convert_to_bytes())

        self.sequence_number += 1
        
        
