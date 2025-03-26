# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ObjectData:
	ID: "U32"


class KillObject(Message):

	absolute_id = 16 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ObjectData = [ObjectData(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
			self.ObjectData.append(ObjectData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: KillObject, 
Message Absolute ID: 16
Blocks:
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.ObjectData[i].ID)

		return output