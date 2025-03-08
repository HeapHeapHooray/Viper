class PacketHeaderFlags:
    def __init__(self,is_zero_coded: bool,is_reliable: bool,is_resent: bool,contains_appended_acks: bool):
        self._is_zero_coded = is_zero_coded
        self._is_reliable = is_reliable
        self._is_resent = is_resent
        self._contains_appended_acks = contains_appended_acks
    def is_zero_coded(self) -> bool:
        return self._is_zero_coded
    def is_reliable(self) -> bool:
        return self._is_reliable
    def is_resent(self) -> bool:
        return self._is_resent
    def contains_appended_acks(self) -> bool:
        return self._contains_appended_acks
    def has_no_flags(self) -> bool:
        return not any([self.is_zero_coded(),self.is_reliable(),self.is_resent(),self.contains_appended_acks()])
    def convert_to_byte(self) -> int:
        if self.is_zero_coded():
            return 0x80
        if self.is_reliable():
            return 0x40
        if self.is_resent():
            return 0x20
        if self.contains_appended_acks():
            return 0x10
        return 0x00
    def convert_to_string(self) -> str:
        output = "PacketHeaderFlags(Flags:"
        flag = ""
        if self.is_zero_coded():
            flag = "ZEROCODED"
        if self.is_reliable():
            flag = "RELIABLE"
        if self.is_resent():
            flag = "RESENT"
        if self.contains_appended_acks():
            flag = "CONTAINS_ACKS"

        if len(flag) > 0:
            output = output + " " + flag
        else:
            output = output + " NO_FLAGS"
            
        output = output + ")"

        return output
    
