# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class Data:
	ObjectID: "LLUUID"
	ItemID: "LLUUID"
	FolderID: "LLUUID"


class BuyObjectInventory(Message):

	absolute_id = 4294901863 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.Data = Data(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.Data = Data(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: BuyObjectInventory, 
Message Absolute ID: 4294901863
Blocks:
{self.AgentData}
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.Data.ObjectID,self.Data.ItemID,self.Data.FolderID)

		return output