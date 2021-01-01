from .PacketHeaderFlags import PacketHeaderFlags

def create_from_byte(byte: int) -> PacketHeaderFlags:
    zero_coded,reliable,resent,contains_acks = False,False,False,False
    if byte == 0x80:
        zero_coded = True
    if byte == 0x40:
        reliable = True
    if byte == 0x20:
        resent = True
    if byte == 0x10:
        contains_acks = True

    return PacketHeaderFlags(zero_coded,reliable,resent,contains_acks)
        
