# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	Stamp: "BOOL"

@dataclass
class InventoryData:
	ItemID: "LLUUID"
	FolderID: "LLUUID"
	NewName: "Variable 1"


class MoveInventoryItem(Message):

	absolute_id = 4294902028 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.InventoryData = [InventoryData(*((None,)*3))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.InventoryData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","variable1",],remaining_bytes)
			self.InventoryData.append(InventoryData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: MoveInventoryItem, 
Message Absolute ID: 4294902028
Blocks:
{self.AgentData}
{self.InventoryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.Stamp)

		blocks_count = len(self.InventoryData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","variable1",],self.InventoryData[i].ItemID,self.InventoryData[i].FolderID,self.InventoryData[i].NewName)

		return output