import BytesUtils
import Utils

class Packet:
    def __init__(self,packet_header,message):
        self.header = packet_header
        self.message = message
    def convert_to_bytes(self) -> bytes:
        message_id_and_message = BytesUtils.pack_bytes_big_endian(["smallest unsigned int"],self.message.absolute_id) + self.message.convert_to_bytes()
        body = message_id_and_message
        if hasattr(self.message,"force_zerocode"):
            if self.message.force_zerocode == True:
                body = Utils.zero_encode(message_id_and_message)
        if self.header.flags.is_zero_coded():
            body = Utils.zero_encode(message_id_and_message)
        return self.header.convert_to_bytes() + body
    def convert_to_string(self):
        return "Packet Header: ["+self.header.convert_to_string()+"] , Message: ["+self.message.convert_to_string()+"]"

