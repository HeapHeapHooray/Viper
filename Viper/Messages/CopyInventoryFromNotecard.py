# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class NotecardData:
	NotecardItemID: "LLUUID"
	ObjectID: "LLUUID"
NOTECARDDATA = NotecardData

@dataclass
class InventoryData:
	ItemID: "LLUUID"
	FolderID: "LLUUID"
INVENTORYDATA = InventoryData


class CopyInventoryFromNotecard(Message):

	absolute_id = 4294902025 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*2))
		self.NotecardData = NOTECARDDATA(*((None,)*2))
		self.InventoryData = [INVENTORYDATA(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.NotecardData = NOTECARDDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.InventoryData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
			self.InventoryData.append(INVENTORYDATA(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: CopyInventoryFromNotecard, 
Message Absolute ID: 4294902025
Blocks:
{self.AgentData}
{self.NotecardData}
{self.InventoryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.NotecardData.NotecardItemID,self.NotecardData.ObjectID)

		blocks_count = len(self.InventoryData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.InventoryData[i].ItemID,self.InventoryData[i].FolderID)

		return output