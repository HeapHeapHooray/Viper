# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class RegionData:
	RegionHandle: "U64"
	TimeDilation: "U16"

@dataclass
class ObjectData:
	Data: "Variable 1"
	TextureEntry: "Variable 2"


class ImprovedTerseObjectUpdate(Message):

	absolute_id = 15 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.RegionData = RegionData(*((None,)*2))
		self.ObjectData = [ObjectData(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","unsigned int16",],remaining_bytes)
		self.RegionData = RegionData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","variable2",],remaining_bytes)
			self.ObjectData.append(ObjectData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ImprovedTerseObjectUpdate, 
Message Absolute ID: 15
Blocks:
{self.RegionData}
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","unsigned int16",],self.RegionData.RegionHandle,self.RegionData.TimeDilation)

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable1","variable2",],self.ObjectData[i].Data,self.ObjectData[i].TextureEntry)

		return output