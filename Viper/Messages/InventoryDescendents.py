# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	FolderID: "LLUUID"
	OwnerID: "LLUUID"
	Version: "S32"
	Descendents: "S32"

@dataclass
class FolderData:
	FolderID: "LLUUID"
	ParentID: "LLUUID"
	Type: "S8"
	Name: "Variable 1"

@dataclass
class ItemData:
	ItemID: "LLUUID"
	FolderID: "LLUUID"
	CreatorID: "LLUUID"
	OwnerID: "LLUUID"
	GroupID: "LLUUID"
	BaseMask: "U32"
	OwnerMask: "U32"
	GroupMask: "U32"
	EveryoneMask: "U32"
	NextOwnerMask: "U32"
	GroupOwned: "BOOL"
	AssetID: "LLUUID"
	Type: "S8"
	InvType: "S8"
	Flags: "U32"
	SaleType: "U8"
	SalePrice: "S32"
	Name: "Variable 1"
	Description: "Variable 1"
	CreationDate: "S32"
	CRC: "U32"


class InventoryDescendents(Message):

	absolute_id = 4294902038 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*5))
		self.FolderData = [FolderData(*((None,)*4))]
		self.ItemData = [ItemData(*((None,)*21))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","signed int32","signed int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.FolderData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","signed byte","variable1",],remaining_bytes)
			self.FolderData.append(FolderData(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ItemData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte","uuid","signed byte","signed byte","unsigned int32","unsigned byte","signed int32","variable1","variable1","signed int32","unsigned int32",],remaining_bytes)
			self.ItemData.append(ItemData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: InventoryDescendents, 
Message Absolute ID: 4294902038
Blocks:
{self.AgentData}
{self.FolderData}
{self.ItemData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","signed int32","signed int32",],self.AgentData.AgentID,self.AgentData.FolderID,self.AgentData.OwnerID,self.AgentData.Version,self.AgentData.Descendents)

		blocks_count = len(self.FolderData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","signed byte","variable1",],self.FolderData[i].FolderID,self.FolderData[i].ParentID,self.FolderData[i].Type,self.FolderData[i].Name)

		blocks_count = len(self.ItemData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte","uuid","signed byte","signed byte","unsigned int32","unsigned byte","signed int32","variable1","variable1","signed int32","unsigned int32",],self.ItemData[i].ItemID,self.ItemData[i].FolderID,self.ItemData[i].CreatorID,self.ItemData[i].OwnerID,self.ItemData[i].GroupID,self.ItemData[i].BaseMask,self.ItemData[i].OwnerMask,self.ItemData[i].GroupMask,self.ItemData[i].EveryoneMask,self.ItemData[i].NextOwnerMask,self.ItemData[i].GroupOwned,self.ItemData[i].AssetID,self.ItemData[i].Type,self.ItemData[i].InvType,self.ItemData[i].Flags,self.ItemData[i].SaleType,self.ItemData[i].SalePrice,self.ItemData[i].Name,self.ItemData[i].Description,self.ItemData[i].CreationDate,self.ItemData[i].CRC)

		return output