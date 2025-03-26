# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class Data:
	GroupID: "LLUUID"
	IsGroupOwned: "BOOL"
	RemoveContribution: "BOOL"
	LocalID: "S32"
	Final: "BOOL"

@dataclass
class ParcelData:
	Price: "S32"
	Area: "S32"


class ParcelBuy(Message):

	absolute_id = 4294901973 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.Data = Data(*((None,)*5))
		self.ParcelData = ParcelData(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte","unsigned byte","signed int32","unsigned byte",],remaining_bytes)
		self.Data = Data(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","signed int32",],remaining_bytes)
		self.ParcelData = ParcelData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelBuy, 
Message Absolute ID: 4294901973
Blocks:
{self.AgentData}
{self.Data}
{self.ParcelData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte","unsigned byte","signed int32","unsigned byte",],self.Data.GroupID,self.Data.IsGroupOwned,self.Data.RemoveContribution,self.Data.LocalID,self.Data.Final)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","signed int32",],self.ParcelData.Price,self.ParcelData.Area)

		return output