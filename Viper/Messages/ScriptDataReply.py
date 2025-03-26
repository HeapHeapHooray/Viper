# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	Hash: "U64"
	Reply: "Variable 2"


class ScriptDataReply(Message):

	absolute_id = 4294902098 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = [DataBlock(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.DataBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","variable2",],remaining_bytes)
			self.DataBlock.append(DataBlock(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ScriptDataReply, 
Message Absolute ID: 4294902098
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.DataBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","variable2",],self.DataBlock[i].Hash,self.DataBlock[i].Reply)

		return output