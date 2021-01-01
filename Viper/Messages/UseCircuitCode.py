from Message.Message import Message
import BytesPack

class UseCircuitCode(Message):
    absolute_id = 4294901763
    def __init__(self,bytes_data: bytes):
        self.circuit_code,self.session_uuid,self.agent_uuid = None,None,None
        if bytes_data is None:
            return
        result = BytesPack.unpack_bytes_little_endian(["unsigned int32","uuid","uuid"],bytes_data)
        self.circuit_code,self.session_uuid,self.agent_uuid = result.unpacked_data
    def convert_to_string(self) -> str:
        return "Message Type: UseCircuitCode , Message Absolute ID: {} , Circuit Code: {} , Session UUID: {} , Agent UUID: {}".format(UseCircuitCode.absolute_id,self.circuit_code,self.session_uuid,self.agent_uuid)
    def convert_to_bytes(self) -> bytes:
        return BytesPack.pack_bytes_little_endian(["unsigned int32","uuid","uuid"],self.circuit_code,self.session_uuid,self.agent_uuid)
