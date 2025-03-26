# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class UUIDNameBlock:
	ID: "LLUUID"
	GroupName: "Variable 1"


class UUIDGroupNameReply(Message):

	absolute_id = 4294901998 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.UUIDNameBlock = [UUIDNameBlock(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.UUIDNameBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1",],remaining_bytes)
			self.UUIDNameBlock.append(UUIDNameBlock(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: UUIDGroupNameReply, 
Message Absolute ID: 4294901998
Blocks:
{self.UUIDNameBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.UUIDNameBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1",],self.UUIDNameBlock[i].ID,self.UUIDNameBlock[i].GroupName)

		return output