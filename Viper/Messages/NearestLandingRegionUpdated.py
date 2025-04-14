# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class RegionData:
	RegionHandle: "U64"
REGIONDATA = RegionData


class NearestLandingRegionUpdated(Message):

	absolute_id = 4294901906 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.RegionData = REGIONDATA(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64",],remaining_bytes)
		self.RegionData = REGIONDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: NearestLandingRegionUpdated, 
Message Absolute ID: 4294901906
Blocks:
{self.RegionData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64",],self.RegionData.RegionHandle)

		return output