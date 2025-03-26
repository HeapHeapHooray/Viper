# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ObjectData:
	ObjectID: "LLUUID"
	CreatorID: "LLUUID"
	OwnerID: "LLUUID"
	GroupID: "LLUUID"
	CreationDate: "U64"
	BaseMask: "U32"
	OwnerMask: "U32"
	GroupMask: "U32"
	EveryoneMask: "U32"
	NextOwnerMask: "U32"
	OwnershipCost: "S32"
	SaleType: "U8"
	SalePrice: "S32"
	AggregatePerms: "U8"
	AggregatePermTextures: "U8"
	AggregatePermTexturesOwner: "U8"
	Category: "U32"
	InventorySerial: "S16"
	ItemID: "LLUUID"
	FolderID: "LLUUID"
	FromTaskID: "LLUUID"
	LastOwnerID: "LLUUID"
	Name: "Variable 1"
	Description: "Variable 1"
	TouchName: "Variable 1"
	SitName: "Variable 1"
	TextureID: "Variable 1"


class ObjectProperties(Message):

	absolute_id = 65289 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ObjectData = [ObjectData(*((None,)*27))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","uuid","unsigned int64","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","signed int32","unsigned byte","signed int32","unsigned byte","unsigned byte","unsigned byte","unsigned int32","signed int16","uuid","uuid","uuid","uuid","variable1","variable1","variable1","variable1","variable1",],remaining_bytes)
			self.ObjectData.append(ObjectData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectProperties, 
Message Absolute ID: 65289
Blocks:
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","uuid","unsigned int64","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","signed int32","unsigned byte","signed int32","unsigned byte","unsigned byte","unsigned byte","unsigned int32","signed int16","uuid","uuid","uuid","uuid","variable1","variable1","variable1","variable1","variable1",],self.ObjectData[i].ObjectID,self.ObjectData[i].CreatorID,self.ObjectData[i].OwnerID,self.ObjectData[i].GroupID,self.ObjectData[i].CreationDate,self.ObjectData[i].BaseMask,self.ObjectData[i].OwnerMask,self.ObjectData[i].GroupMask,self.ObjectData[i].EveryoneMask,self.ObjectData[i].NextOwnerMask,self.ObjectData[i].OwnershipCost,self.ObjectData[i].SaleType,self.ObjectData[i].SalePrice,self.ObjectData[i].AggregatePerms,self.ObjectData[i].AggregatePermTextures,self.ObjectData[i].AggregatePermTexturesOwner,self.ObjectData[i].Category,self.ObjectData[i].InventorySerial,self.ObjectData[i].ItemID,self.ObjectData[i].FolderID,self.ObjectData[i].FromTaskID,self.ObjectData[i].LastOwnerID,self.ObjectData[i].Name,self.ObjectData[i].Description,self.ObjectData[i].TouchName,self.ObjectData[i].SitName,self.ObjectData[i].TextureID)

		return output