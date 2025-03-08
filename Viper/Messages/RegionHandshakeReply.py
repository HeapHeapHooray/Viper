from Message.Message import Message
import BytesUtils

class RegionHandshakeReply(Message):
    absolute_id = 4294901909
    def __init__(self,bytes_data: bytes):
        self.agent_uuid,self.session_uuid,self.region_info_flags = None,None,None
        if bytes_data is None:
            return
        result = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32"],bytes_data)
        self.agent_uuid,self.session_uuid,self.region_info_flags = result.unpacked_data
    def convert_to_string(self) -> str:
        return "Message Type: RegionHandshakeReply , Message Absolute ID: {} , Agent UUID: {} , Session UUID: {} , Region Info Flags: {}".format(RegionHandshakeReply.absolute_id,self.agent_uuid,self.session_uuid,self.region_info_flags)
    def convert_to_bytes(self) -> bytes:
        return BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32"],self.agent_uuid,self.session_uuid,self.region_info_flags)
