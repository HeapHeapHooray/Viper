import BytesUtils

class Packet:
    def __init__(self,packet_header,message):
        self.header = packet_header
        self.message = message
    def convert_to_bytes(self) -> bytes:
        return self.header.convert_to_bytes() + BytesUtils.pack_bytes_big_endian(["unsigned int32"],self.message.absolute_id) + self.message.convert_to_bytes()
    def convert_to_string(self):
        return "Packet Header: ["+self.header.convert_to_string()+"] , Message: ["+self.message.convert_to_string()+"]"

