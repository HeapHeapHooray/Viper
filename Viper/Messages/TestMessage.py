# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TestBlock1:
	Test1: "U32"

@dataclass
class NeighborBlock:
	Test0: "U32"
	Test1: "U32"
	Test2: "U32"


class TestMessage(Message):

	absolute_id = 4294901761 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TestBlock1 = TestBlock1(*((None,)*1))
		self.NeighborBlock = []
		for i in range(4):
			self.NeighborBlock.append(NeighborBlock(*((None,)*3)))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
		self.TestBlock1 = TestBlock1(*unpacked_data)

		blocks_count = 4 # -- Fixed/constant Blocks length of 4. 

		self.NeighborBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
			self.NeighborBlock.append(NeighborBlock(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: TestMessage, 
Message Absolute ID: 4294901761
Blocks:
{self.TestBlock1}
{self.NeighborBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.TestBlock1.Test1)

		blocks_count = 4

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32",],self.NeighborBlock[i].Test0,self.NeighborBlock[i].Test1,self.NeighborBlock[i].Test2)

		return output