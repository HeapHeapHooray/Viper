# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class RegionInfo:
	SimName: "Variable 1"
	EstateID: "U32"
	ParentEstateID: "U32"
	RegionFlags: "U32"
	BillableFactor: "F32"
	PricePerMeter: "S32"
	RedirectGridX: "S32"
	RedirectGridY: "S32"

@dataclass
class RegionInfo2:
	RegionFlagsExtended: "U64"


class GodUpdateRegionInfo(Message):

	absolute_id = 4294901903 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.RegionInfo = RegionInfo(*((None,)*8))
		self.RegionInfo2 = [RegionInfo2(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","unsigned int32","unsigned int32","unsigned int32","float","signed int32","signed int32","signed int32",],remaining_bytes)
		self.RegionInfo = RegionInfo(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.RegionInfo2 = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64",],remaining_bytes)
			self.RegionInfo2.append(RegionInfo2(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: GodUpdateRegionInfo, 
Message Absolute ID: 4294901903
Blocks:
{self.AgentData}
{self.RegionInfo}
{self.RegionInfo2}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","unsigned int32","unsigned int32","unsigned int32","float","signed int32","signed int32","signed int32",],self.RegionInfo.SimName,self.RegionInfo.EstateID,self.RegionInfo.ParentEstateID,self.RegionInfo.RegionFlags,self.RegionInfo.BillableFactor,self.RegionInfo.PricePerMeter,self.RegionInfo.RedirectGridX,self.RegionInfo.RedirectGridY)

		blocks_count = len(self.RegionInfo2)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64",],self.RegionInfo2[i].RegionFlagsExtended)

		return output