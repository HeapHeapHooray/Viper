from . import PacketHeaderFactory
from . import Packet
import Message
import Utils

def create_from_bytes(bytes_data: bytes):
    packet_header = PacketHeaderFactory.create_from_bytes(bytes_data)
    
    message_data = bytes_data[packet_header.get_data_size_as_bytes()::]
    unencoded_message_data = message_data
    if packet_header.flags.is_zero_coded():
        unencoded_message_data = Utils.zero_decode(message_data)
    message = Message.MessageFactory.create_from_bytes(unencoded_message_data)

    packet = Packet.Packet(packet_header,message)

    return packet

    
