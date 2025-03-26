# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentBlock:
	AgentID: "LLUUID"


class OfflineNotification(Message):

	absolute_id = 4294902083 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentBlock = [AgentBlock(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AgentBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.AgentBlock.append(AgentBlock(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: OfflineNotification, 
Message Absolute ID: 4294902083
Blocks:
{self.AgentBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.AgentBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentBlock[i].AgentID)

		return output