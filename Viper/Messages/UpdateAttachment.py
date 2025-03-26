# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class AttachmentBlock:
	AttachmentPoint: "U8"

@dataclass
class OperationData:
	AddItem: "BOOL"
	UseExistingAsset: "BOOL"

@dataclass
class InventoryData:
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


class UpdateAttachment(Message):

	absolute_id = 4294902091 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.AttachmentBlock = AttachmentBlock(*((None,)*1))
		self.OperationData = OperationData(*((None,)*2))
		self.InventoryData = InventoryData(*((None,)*21))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
		self.AttachmentBlock = AttachmentBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned byte",],remaining_bytes)
		self.OperationData = OperationData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte","uuid","signed byte","signed byte","unsigned int32","unsigned byte","signed int32","variable1","variable1","signed int32","unsigned int32",],remaining_bytes)
		self.InventoryData = InventoryData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: UpdateAttachment, 
Message Absolute ID: 4294902091
Blocks:
{self.AgentData}
{self.AttachmentBlock}
{self.OperationData}
{self.InventoryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.AttachmentBlock.AttachmentPoint)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned byte",],self.OperationData.AddItem,self.OperationData.UseExistingAsset)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte","uuid","signed byte","signed byte","unsigned int32","unsigned byte","signed int32","variable1","variable1","signed int32","unsigned int32",],self.InventoryData.ItemID,self.InventoryData.FolderID,self.InventoryData.CreatorID,self.InventoryData.OwnerID,self.InventoryData.GroupID,self.InventoryData.BaseMask,self.InventoryData.OwnerMask,self.InventoryData.GroupMask,self.InventoryData.EveryoneMask,self.InventoryData.NextOwnerMask,self.InventoryData.GroupOwned,self.InventoryData.AssetID,self.InventoryData.Type,self.InventoryData.InvType,self.InventoryData.Flags,self.InventoryData.SaleType,self.InventoryData.SalePrice,self.InventoryData.Name,self.InventoryData.Description,self.InventoryData.CreationDate,self.InventoryData.CRC)

		return output