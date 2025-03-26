# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"

@dataclass
class Data:
	ParcelID: "LLUUID"
	OwnerID: "LLUUID"
	Name: "Variable 1"
	Desc: "Variable 1"
	ActualArea: "S32"
	BillableArea: "S32"
	Flags: "U8"
	GlobalX: "F32"
	GlobalY: "F32"
	GlobalZ: "F32"
	SimName: "Variable 1"
	SnapshotID: "LLUUID"
	Dwell: "F32"
	SalePrice: "S32"
	AuctionID: "S32"


class ParcelInfoReply(Message):

	absolute_id = 4294901815 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.Data = Data(*((None,)*15))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","variable1","variable1","signed int32","signed int32","unsigned byte","float","float","float","variable1","uuid","float","signed int32","signed int32",],remaining_bytes)
		self.Data = Data(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelInfoReply, 
Message Absolute ID: 4294901815
Blocks:
{self.AgentData}
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","variable1","variable1","signed int32","signed int32","unsigned byte","float","float","float","variable1","uuid","float","signed int32","signed int32",],self.Data.ParcelID,self.Data.OwnerID,self.Data.Name,self.Data.Desc,self.Data.ActualArea,self.Data.BillableArea,self.Data.Flags,self.Data.GlobalX,self.Data.GlobalY,self.Data.GlobalZ,self.Data.SimName,self.Data.SnapshotID,self.Data.Dwell,self.Data.SalePrice,self.Data.AuctionID)

		return output