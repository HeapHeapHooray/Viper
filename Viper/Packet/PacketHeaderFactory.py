import BytesPack
from .PacketHeader import PacketHeader
from . import PacketHeaderFlagsFactory

def create_from_bytes(bytes_data: bytes):
    unpack_result = BytesPack.unpack_bytes_big_endian(["unsigned byte","unsigned int32","unsigned byte"],bytes_data)
    byte_flags,sequence_number,extra_bytes_count = unpack_result.unpacked_data

    flags = PacketHeaderFlagsFactory.create_from_byte(byte_flags)
    extra_bytes = b""
    if extra_bytes_count > 0:
        extra_bytes = unpack_result.remaining_bytes[::extra_bytes_count]
    packet_header = PacketHeader(flags,sequence_number,extra_bytes)

    return packet_header
    #print("Flags:",byte_flags,"Sequence Number:",sequence_number,"Extra Bytes Count:",extra_bytes_count)
