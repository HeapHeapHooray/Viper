# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	FromAgentId: "LLUUID"
	ToAgentId: "LLUUID"
	GlobalX: "F64"
	GlobalY: "F64"
	Time: "U32"
	Message: "Variable 2"


class LogTextMessage(Message):

	absolute_id = 4294902151 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = [DataBlock(*((None,)*6))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.DataBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","double","double","unsigned int32","variable2",],remaining_bytes)
			self.DataBlock.append(DataBlock(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: LogTextMessage, 
Message Absolute ID: 4294902151
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.DataBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","double","double","unsigned int32","variable2",],self.DataBlock[i].FromAgentId,self.DataBlock[i].ToAgentId,self.DataBlock[i].GlobalX,self.DataBlock[i].GlobalY,self.DataBlock[i].Time,self.DataBlock[i].Message)

		return output