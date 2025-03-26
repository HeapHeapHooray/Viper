# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentBlock:
	SourceID: "LLUUID"
	DestID: "LLUUID"


class FormFriendship(Message):

	absolute_id = 4294902059 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentBlock = AgentBlock(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentBlock = AgentBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: FormFriendship, 
Message Absolute ID: 4294902059
Blocks:
{self.AgentBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentBlock.SourceID,self.AgentBlock.DestID)

		return output