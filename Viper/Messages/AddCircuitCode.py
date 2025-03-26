# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class CircuitCode:
	Code: "U32"
	SessionID: "LLUUID"
	AgentID: "LLUUID"


class AddCircuitCode(Message):

	absolute_id = 4294901762 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.CircuitCode = CircuitCode(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","uuid","uuid",],remaining_bytes)
		self.CircuitCode = CircuitCode(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AddCircuitCode, 
Message Absolute ID: 4294901762
Blocks:
{self.CircuitCode}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","uuid","uuid",],self.CircuitCode.Code,self.CircuitCode.SessionID,self.CircuitCode.AgentID)

		return output