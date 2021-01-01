from Message.Message import Message
import BytesPack

class CompleteAgentMovement(Message):
    absolute_id = 4294902009
    def __init__(self,bytes_data: bytes):
        self.agent_uuid,self.session_uuid,self.circuit_code = None,None,None
        if bytes_data is None:
            return
        result = BytesPack.unpack_bytes_little_endian(["uuid","uuid","unsigned int32"],bytes_data)
        self.agent_uuid,self.session_uuid,self.circuit_code = result.unpacked_data
    def convert_to_string(self) -> str:
        return "Message Type: CompleteAgentMovement , Message Absolute ID: {} , Agent UUID: {} , Session UUID: {} , Circuit Code: {}".format(CompleteAgentMovement.absolute_id,self.agent_uuid,self.session_uuid,self.circuit_code)
    def convert_to_bytes(self) -> bytes:
        return BytesPack.pack_bytes_little_endian(["uuid","uuid","unsigned int32"],self.agent_uuid,self.session_uuid,self.circuit_code)
    
        
