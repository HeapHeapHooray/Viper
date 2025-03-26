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
class RezData:
	FromTaskID: "LLUUID"
	BypassRaycast: "U8"
	RayStart: "LLVector3"
	RayEnd: "LLVector3"
	RayTargetID: "LLUUID"
	RayEndIsIntersection: "BOOL"
	RezSelected: "BOOL"
	RemoveItem: "BOOL"
	ItemFlags: "U32"
	GroupMask: "U32"
	EveryoneMask: "U32"
	NextOwnerMask: "U32"

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


class RezObject(Message):

	absolute_id = 4294902053 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.RezData = RezData(*((None,)*12))
		self.InventoryData = InventoryData(*((None,)*21))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte","vector3","vector3","uuid","unsigned byte","unsigned byte","unsigned byte","unsigned int32","unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
		self.RezData = RezData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte","uuid","signed byte","signed byte","unsigned int32","unsigned byte","signed int32","variable1","variable1","signed int32","unsigned int32",],remaining_bytes)
		self.InventoryData = InventoryData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RezObject, 
Message Absolute ID: 4294902053
Blocks:
{self.AgentData}
{self.RezData}
{self.InventoryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte","vector3","vector3","uuid","unsigned byte","unsigned byte","unsigned byte","unsigned int32","unsigned int32","unsigned int32","unsigned int32",],self.RezData.FromTaskID,self.RezData.BypassRaycast,self.RezData.RayStart,self.RezData.RayEnd,self.RezData.RayTargetID,self.RezData.RayEndIsIntersection,self.RezData.RezSelected,self.RezData.RemoveItem,self.RezData.ItemFlags,self.RezData.GroupMask,self.RezData.EveryoneMask,self.RezData.NextOwnerMask)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte","uuid","signed byte","signed byte","unsigned int32","unsigned byte","signed int32","variable1","variable1","signed int32","unsigned int32",],self.InventoryData.ItemID,self.InventoryData.FolderID,self.InventoryData.CreatorID,self.InventoryData.OwnerID,self.InventoryData.GroupID,self.InventoryData.BaseMask,self.InventoryData.OwnerMask,self.InventoryData.GroupMask,self.InventoryData.EveryoneMask,self.InventoryData.NextOwnerMask,self.InventoryData.GroupOwned,self.InventoryData.TransactionID,self.InventoryData.Type,self.InventoryData.InvType,self.InventoryData.Flags,self.InventoryData.SaleType,self.InventoryData.SalePrice,self.InventoryData.Name,self.InventoryData.Description,self.InventoryData.CreationDate,self.InventoryData.CRC)

		return output