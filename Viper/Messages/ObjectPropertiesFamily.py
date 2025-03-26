# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ObjectData:
	RequestFlags: "U32"
	ObjectID: "LLUUID"
	OwnerID: "LLUUID"
	GroupID: "LLUUID"
	BaseMask: "U32"
	OwnerMask: "U32"
	GroupMask: "U32"
	EveryoneMask: "U32"
	NextOwnerMask: "U32"
	OwnershipCost: "S32"
	SaleType: "U8"
	SalePrice: "S32"
	Category: "U32"
	LastOwnerID: "LLUUID"
	Name: "Variable 1"
	Description: "Variable 1"


class ObjectPropertiesFamily(Message):

	absolute_id = 65290 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ObjectData = ObjectData(*((None,)*16))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","signed int32","unsigned byte","signed int32","unsigned int32","uuid","variable1","variable1",],remaining_bytes)
		self.ObjectData = ObjectData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectPropertiesFamily, 
Message Absolute ID: 65290
Blocks:
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","signed int32","unsigned byte","signed int32","unsigned int32","uuid","variable1","variable1",],self.ObjectData.RequestFlags,self.ObjectData.ObjectID,self.ObjectData.OwnerID,self.ObjectData.GroupID,self.ObjectData.BaseMask,self.ObjectData.OwnerMask,self.ObjectData.GroupMask,self.ObjectData.EveryoneMask,self.ObjectData.NextOwnerMask,self.ObjectData.OwnershipCost,self.ObjectData.SaleType,self.ObjectData.SalePrice,self.ObjectData.Category,self.ObjectData.LastOwnerID,self.ObjectData.Name,self.ObjectData.Description)

		return output