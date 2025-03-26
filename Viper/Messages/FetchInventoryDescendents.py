# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class InventoryData:
	FolderID: "LLUUID"
	OwnerID: "LLUUID"
	SortOrder: "S32"
	FetchFolders: "BOOL"
	FetchItems: "BOOL"


class FetchInventoryDescendents(Message):

	absolute_id = 4294902037 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.InventoryData = InventoryData(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","signed int32","unsigned byte","unsigned byte",],remaining_bytes)
		self.InventoryData = InventoryData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: FetchInventoryDescendents, 
Message Absolute ID: 4294902037
Blocks:
{self.AgentData}
{self.InventoryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","signed int32","unsigned byte","unsigned byte",],self.InventoryData.FolderID,self.InventoryData.OwnerID,self.InventoryData.SortOrder,self.InventoryData.FetchFolders,self.InventoryData.FetchItems)

		return output