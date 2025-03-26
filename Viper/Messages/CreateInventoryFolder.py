# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class FolderData:
	FolderID: "LLUUID"
	ParentID: "LLUUID"
	Type: "S8"
	Name: "Variable 1"


class CreateInventoryFolder(Message):

	absolute_id = 4294902033 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.FolderData = FolderData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","signed byte","variable1",],remaining_bytes)
		self.FolderData = FolderData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: CreateInventoryFolder, 
Message Absolute ID: 4294902033
Blocks:
{self.AgentData}
{self.FolderData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","signed byte","variable1",],self.FolderData.FolderID,self.FolderData.ParentID,self.FolderData.Type,self.FolderData.Name)

		return output