# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class InventoryBlock:
	CallbackID: "U32"
	FolderID: "LLUUID"
	TransactionID: "LLUUID"
	OldItemID: "LLUUID"
	Type: "S8"
	InvType: "S8"
	Name: "Variable 1"
	Description: "Variable 1"


class LinkInventoryItem(Message):

	absolute_id = 4294902186 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.InventoryBlock = InventoryBlock(*((None,)*8))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","uuid","uuid","uuid","signed byte","signed byte","variable1","variable1",],remaining_bytes)
		self.InventoryBlock = InventoryBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: LinkInventoryItem, 
Message Absolute ID: 4294902186
Blocks:
{self.AgentData}
{self.InventoryBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","uuid","uuid","uuid","signed byte","signed byte","variable1","variable1",],self.InventoryBlock.CallbackID,self.InventoryBlock.FolderID,self.InventoryBlock.TransactionID,self.InventoryBlock.OldItemID,self.InventoryBlock.Type,self.InventoryBlock.InvType,self.InventoryBlock.Name,self.InventoryBlock.Description)

		return output