# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ReplyData:
	RequestID: "LLUUID"
	GroupID: "LLUUID"
	Selection: "Variable 1"


class LiveHelpGroupReply(Message):

	absolute_id = 4294902140 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ReplyData = ReplyData(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","variable1",],remaining_bytes)
		self.ReplyData = ReplyData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: LiveHelpGroupReply, 
Message Absolute ID: 4294902140
Blocks:
{self.ReplyData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","variable1",],self.ReplyData.RequestID,self.ReplyData.GroupID,self.ReplyData.Selection)

		return output