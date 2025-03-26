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
	ID: "U32"
	CRC: "U32"
	UpdateFlags: "U32"


class ObjectUpdateCached(Message):

	absolute_id = 14 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.RegionData = RegionData(*((None,)*2))
		self.ObjectData = [ObjectData(*((None,)*3))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","unsigned int16",],remaining_bytes)
		self.RegionData = RegionData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
			self.ObjectData.append(ObjectData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectUpdateCached, 
Message Absolute ID: 14
Blocks:
{self.RegionData}
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","unsigned int16",],self.RegionData.RegionHandle,self.RegionData.TimeDilation)

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32",],self.ObjectData[i].ID,self.ObjectData[i].CRC,self.ObjectData[i].UpdateFlags)

		return output