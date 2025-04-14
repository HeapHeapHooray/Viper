# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class MessageBlock:
	ToGroupID: "LLUUID"
	ID: "LLUUID"
	Dialog: "U8"
	FromAgentName: "Variable 1"
	Message: "Variable 2"
	BinaryBucket: "Variable 2"
MESSAGEBLOCK = MessageBlock


class GroupNoticeAdd(Message):

	absolute_id = 4294901821 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*1))

		self.MessageBlock = MESSAGEBLOCK(*((None,)*6))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte","variable1","variable2","variable2",],remaining_bytes)
		self.MessageBlock = MESSAGEBLOCK(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupNoticeAdd, Message Absolute ID: 4294901821, Blocks: {self.AgentData},{self.MessageBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte","variable1","variable2","variable2",],self.MessageBlock.ToGroupID,self.MessageBlock.ID,self.MessageBlock.Dialog,self.MessageBlock.FromAgentName,self.MessageBlock.Message,self.MessageBlock.BinaryBucket)

		return output