import BytesUtils
import Utils

class Packet:
    def __init__(self,packet_header,message):
        self.header = packet_header
        self.message = message
    def convert_to_bytes(self) -> bytes:
        message_id_and_message = BytesUtils.pack_bytes_big_endian(["smallest unsigned int"],self.message.absolute_id) + self.message.convert_to_bytes()
        body_bytes = message_id_and_message
        if hasattr(self.message,"force_zerocode"):
            if self.message.force_zerocode == True:
                body_bytes = Utils.zero_encode(message_id_and_message)
        if self.header.flags.is_zero_coded():
            body_bytes = Utils.zero_encode(message_id_and_message)
        head_bytes = self.header.convert_to_bytes()
        return head_bytes + body_bytes
    def convert_to_string(self):
        return "Packet Header: ["+self.header.convert_to_string()+"] , Message: ["+self.message.convert_to_string()+"]"

