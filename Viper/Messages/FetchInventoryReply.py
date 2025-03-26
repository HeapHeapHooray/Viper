# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"

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


class FetchInventoryReply(Message):

	absolute_id = 4294902040 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.InventoryData = [InventoryData(*((None,)*21))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.InventoryData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte","uuid","signed byte","signed byte","unsigned int32","unsigned byte","signed int32","variable1","variable1","signed int32","unsigned int32",],remaining_bytes)
			self.InventoryData.append(InventoryData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: FetchInventoryReply, 
Message Absolute ID: 4294902040
Blocks:
{self.AgentData}
{self.InventoryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		blocks_count = len(self.InventoryData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","uuid","uuid","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte","uuid","signed byte","signed byte","unsigned int32","unsigned byte","signed int32","variable1","variable1","signed int32","unsigned int32",],self.InventoryData[i].ItemID,self.InventoryData[i].FolderID,self.InventoryData[i].CreatorID,self.InventoryData[i].OwnerID,self.InventoryData[i].GroupID,self.InventoryData[i].BaseMask,self.InventoryData[i].OwnerMask,self.InventoryData[i].GroupMask,self.InventoryData[i].EveryoneMask,self.InventoryData[i].NextOwnerMask,self.InventoryData[i].GroupOwned,self.InventoryData[i].AssetID,self.InventoryData[i].Type,self.InventoryData[i].InvType,self.InventoryData[i].Flags,self.InventoryData[i].SaleType,self.InventoryData[i].SalePrice,self.InventoryData[i].Name,self.InventoryData[i].Description,self.InventoryData[i].CreationDate,self.InventoryData[i].CRC)

		return output