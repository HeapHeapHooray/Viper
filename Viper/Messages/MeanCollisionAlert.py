# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class MeanCollision:
	Victim: "LLUUID"
	Perp: "LLUUID"
	Time: "U32"
	Mag: "F32"
	Type: "U8"


class MeanCollisionAlert(Message):

	absolute_id = 4294901896 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.MeanCollision = [MeanCollision(*((None,)*5))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.MeanCollision = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32","float","unsigned byte",],remaining_bytes)
			self.MeanCollision.append(MeanCollision(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: MeanCollisionAlert, 
Message Absolute ID: 4294901896
Blocks:
{self.MeanCollision}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.MeanCollision)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32","float","unsigned byte",],self.MeanCollision[i].Victim,self.MeanCollision[i].Perp,self.MeanCollision[i].Time,self.MeanCollision[i].Mag,self.MeanCollision[i].Type)

		return output