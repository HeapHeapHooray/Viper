# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class EventData:
	EventID: "U32"
EVENTDATA = EventData

@dataclass
class InventoryBlock:
	FolderID: "LLUUID"
	Name: "Variable 1"
INVENTORYBLOCK = InventoryBlock


class CreateLandmarkForEvent(Message):

	absolute_id = 4294902066 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*2))

		self.EventData = EVENTDATA(*((None,)*1))

		self.InventoryBlock = INVENTORYBLOCK(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
		self.EventData = EVENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1",],remaining_bytes)
		self.InventoryBlock = INVENTORYBLOCK(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: CreateLandmarkForEvent, Message Absolute ID: 4294902066, Blocks: {self.AgentData},{self.EventData},{self.InventoryBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.EventData.EventID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1",],self.InventoryBlock.FolderID,self.InventoryBlock.Name)

		return output