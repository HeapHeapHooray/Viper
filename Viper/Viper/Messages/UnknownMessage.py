from Message.Message import Message
import BytesUtils

class UnknownMessage(Message):
    def __init__(self,message_id: int,bytes_data: bytes):
        self.message_id = message_id
        self.data = bytes_data
    def convert_to_string(self) -> str:
        return "Message Type: UnknownMessage , Message Absolute ID: {} , Data: {}".format(self.message_id,self.data)
    def convert_to_bytes(self) -> bytes:
        return BytesUtils.pack_bytes_big_endian(["smallest unsigned int"],self.message_id) + self.data
        
        
