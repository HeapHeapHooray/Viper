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
	ChatChannel: "S32"
	ButtonIndex: "S32"
	ButtonLabel: "Variable 1"


class ScriptDialogReply(Message):

	absolute_id = 4294901951 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.Data = Data(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","signed int32","variable1",],remaining_bytes)
		self.Data = Data(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ScriptDialogReply, 
Message Absolute ID: 4294901951
Blocks:
{self.AgentData}
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","signed int32","variable1",],self.Data.ObjectID,self.Data.ChatChannel,self.Data.ButtonIndex,self.Data.ButtonLabel)

		return output