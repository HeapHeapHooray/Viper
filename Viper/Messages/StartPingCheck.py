from Message.Message import Message
import BytesPack

class StartPingCheck(Message):
    absolute_id = 1
    def __init__(self,bytes_data: bytes):
        result = BytesPack.unpack_bytes_little_endian(["unsigned byte","unsigned int32"],bytes_data)
        self.ping_id,self.oldest_unacked = result.unpacked_data
    def convert_to_string(self) -> str:
        return "Message Type: StartPingCheck , Message Absolute ID: {} , Ping ID: {} , Oldest Unacked Packet: {}".format(StartPingCheck.absolute_id,self.ping_id,self.oldest_unacked)
    def convert_to_bytes(self) -> bytes:
        return BytesPack.pack_bytes_little_endian(["unsigned byte","unsigned int32"],self.ping_id,self.oldest_unacked)
        
        
