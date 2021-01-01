from .PacketHeaderFlags import PacketHeaderFlags
import BytesPack

class PacketHeader:
    def __init__(self,flags: PacketHeaderFlags,sequence_number: int,extra_bytes: bytes):
        self.flags = flags
        self.sequence_number = sequence_number
        self.extra_bytes = extra_bytes
    def get_data_size_as_bytes(self):
        size = BytesPack.calculate_minimum_size(["unsigned byte","unsigned int32","unsigned byte"]) + len(self.extra_bytes)
        return size
    def convert_to_bytes(self) -> bytes:
        return BytesPack.pack_bytes_big_endian(["unsigned byte","unsigned int32","unsigned byte"],self.flags.convert_to_byte(),self.sequence_number,len(self.extra_bytes)) + self.extra_bytes
    def convert_to_string(self) -> str:
        output = "PacketHeader(" + self.flags.convert_to_string()
        output = output + " , " + "Sequence Number: " + str(self.sequence_number)
        output = output + " , " + "Extra Bytes Count: " + str(len(self.extra_bytes))
        if len(self.extra_bytes) > 0:
            output = output + " , " + "Extra Bytes: " + str(self.extra_bytes)

        return output
    
    
