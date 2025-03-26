# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"

@dataclass
class Data:
	ClassifiedID: "LLUUID"
	CreatorID: "LLUUID"
	CreationDate: "U32"
	ExpirationDate: "U32"
	Category: "U32"
	Name: "Variable 1"
	Desc: "Variable 2"
	ParcelID: "LLUUID"
	ParentEstate: "U32"
	SnapshotID: "LLUUID"
	SimName: "Variable 1"
	PosGlobal: "LLVector3d"
	ParcelName: "Variable 1"
	ClassifiedFlags: "U8"
	PriceForListing: "S32"


class ClassifiedInfoReply(Message):

	absolute_id = 4294901804 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.Data = Data(*((None,)*15))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned int32","unsigned int32","variable1","variable2","uuid","unsigned int32","uuid","variable1","vector3d","variable1","unsigned byte","signed int32",],remaining_bytes)
		self.Data = Data(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ClassifiedInfoReply, 
Message Absolute ID: 4294901804
Blocks:
{self.AgentData}
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned int32","unsigned int32","variable1","variable2","uuid","unsigned int32","uuid","variable1","vector3d","variable1","unsigned byte","signed int32",],self.Data.ClassifiedID,self.Data.CreatorID,self.Data.CreationDate,self.Data.ExpirationDate,self.Data.Category,self.Data.Name,self.Data.Desc,self.Data.ParcelID,self.Data.ParentEstate,self.Data.SnapshotID,self.Data.SimName,self.Data.PosGlobal,self.Data.ParcelName,self.Data.ClassifiedFlags,self.Data.PriceForListing)

		return output