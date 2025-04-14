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
class ChatData:
	Message: "Variable 2"
	Type: "U8"
	Channel: "S32"
CHATDATA = ChatData


class ChatFromViewer(Message):

	absolute_id = 4294901840 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*2))

		self.ChatData = CHATDATA(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2","unsigned byte","signed int32",],remaining_bytes)
		self.ChatData = CHATDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ChatFromViewer, Message Absolute ID: 4294901840, Blocks: {self.AgentData},{self.ChatData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["variable2","unsigned byte","signed int32",],self.ChatData.Message,self.ChatData.Type,self.ChatData.Channel)

		return output