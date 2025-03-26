# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"

@dataclass
class RegionData:
	RegionHandle: "U64"

@dataclass
class ParcelData:
	ParcelID: "LLUUID"
	OwnerID: "LLUUID"
	IsOwnerGroup: "BOOL"
	ActualArea: "S32"
	Action: "S8"
	TransactionID: "LLUUID"


class LogParcelChanges(Message):

	absolute_id = 4294901984 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.RegionData = RegionData(*((None,)*1))
		self.ParcelData = [ParcelData(*((None,)*6))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64",],remaining_bytes)
		self.RegionData = RegionData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ParcelData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte","signed int32","signed byte","uuid",],remaining_bytes)
			self.ParcelData.append(ParcelData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: LogParcelChanges, 
Message Absolute ID: 4294901984
Blocks:
{self.AgentData}
{self.RegionData}
{self.ParcelData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64",],self.RegionData.RegionHandle)

		blocks_count = len(self.ParcelData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte","signed int32","signed byte","uuid",],self.ParcelData[i].ParcelID,self.ParcelData[i].OwnerID,self.ParcelData[i].IsOwnerGroup,self.ParcelData[i].ActualArea,self.ParcelData[i].Action,self.ParcelData[i].TransactionID)

		return output