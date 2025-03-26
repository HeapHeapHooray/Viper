# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	GroupID: "LLUUID"

@dataclass
class UpdateBlock:
	ObjectLocalID: "U32"
	Enabled: "BOOL"

@dataclass
class InventoryBlock:
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
	TransactionID: "LLUUID"
	Type: "S8"
	InvType: "S8"
	Flags: "U32"
	SaleType: "U8"
	SalePrice: "S32"
	Name: "Variable 1"
	Description: "Variable 1"
	CreationDate: "S32"
	CRC: "U32"


class RezScript(Message):

	absolute_id = 4294902064 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.UpdateBlock = UpdateBlock(*((None,)*2))
		self.InventoryBlock = InventoryBlock(*((None,)*21))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned byte",],remaining_bytes)
		self.UpdateBlock = UpdateBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte","uuid","signed byte","signed byte","unsigned int32","unsigned byte","signed int32","variable1","variable1","signed int32","unsigned int32",],remaining_bytes)
		self.InventoryBlock = InventoryBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RezScript, 
Message Absolute ID: 4294902064
Blocks:
{self.AgentData}
{self.UpdateBlock}
{self.InventoryBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned byte",],self.UpdateBlock.ObjectLocalID,self.UpdateBlock.Enabled)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte","uuid","signed byte","signed byte","unsigned int32","unsigned byte","signed int32","variable1","variable1","signed int32","unsigned int32",],self.InventoryBlock.ItemID,self.InventoryBlock.FolderID,self.InventoryBlock.CreatorID,self.InventoryBlock.OwnerID,self.InventoryBlock.GroupID,self.InventoryBlock.BaseMask,self.InventoryBlock.OwnerMask,self.InventoryBlock.GroupMask,self.InventoryBlock.EveryoneMask,self.InventoryBlock.NextOwnerMask,self.InventoryBlock.GroupOwned,self.InventoryBlock.TransactionID,self.InventoryBlock.Type,self.InventoryBlock.InvType,self.InventoryBlock.Flags,self.InventoryBlock.SaleType,self.InventoryBlock.SalePrice,self.InventoryBlock.Name,self.InventoryBlock.Description,self.InventoryBlock.CreationDate,self.InventoryBlock.CRC)

		return output