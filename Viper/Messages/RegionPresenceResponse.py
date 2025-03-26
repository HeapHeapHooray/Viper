# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class RegionData:
	RegionID: "LLUUID"
	RegionHandle: "U64"
	InternalRegionIP: "IPADDR"
	ExternalRegionIP: "IPADDR"
	RegionPort: "IPPORT"
	ValidUntil: "F64"
	Message: "Variable 1"


class RegionPresenceResponse(Message):

	absolute_id = 4294901776 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.RegionData = [RegionData(*((None,)*7))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.RegionData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int64","unsigned int32","unsigned int32","unsigned int16","double","variable1",],remaining_bytes)
			self.RegionData.append(RegionData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: RegionPresenceResponse, 
Message Absolute ID: 4294901776
Blocks:
{self.RegionData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.RegionData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int64","unsigned int32","unsigned int32","unsigned int16","double","variable1",],self.RegionData[i].RegionID,self.RegionData[i].RegionHandle,self.RegionData[i].InternalRegionIP,self.RegionData[i].ExternalRegionIP,self.RegionData[i].RegionPort,self.RegionData[i].ValidUntil,self.RegionData[i].Message)

		return output