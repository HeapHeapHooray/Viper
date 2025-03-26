# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	ObjectID: "LLUUID"
	OwnerID: "LLUUID"
	SoundID: "LLUUID"


class PreloadSound(Message):

	absolute_id = 65295 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = [DataBlock(*((None,)*3))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.DataBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
			self.DataBlock.append(DataBlock(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: PreloadSound, 
Message Absolute ID: 65295
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.DataBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.DataBlock[i].ObjectID,self.DataBlock[i].OwnerID,self.DataBlock[i].SoundID)

		return output