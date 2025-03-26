# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ChatData:
	FromName: "Variable 1"
	SourceID: "LLUUID"
	OwnerID: "LLUUID"
	SourceType: "U8"
	ChatType: "U8"
	Audible: "U8"
	Position: "LLVector3"
	Message: "Variable 2"


class ChatFromSimulator(Message):

	absolute_id = 4294901899 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ChatData = ChatData(*((None,)*8))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","uuid","uuid","unsigned byte","unsigned byte","unsigned byte","vector3","variable2",],remaining_bytes)
		self.ChatData = ChatData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ChatFromSimulator, 
Message Absolute ID: 4294901899
Blocks:
{self.ChatData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","uuid","uuid","unsigned byte","unsigned byte","unsigned byte","vector3","variable2",],self.ChatData.FromName,self.ChatData.SourceID,self.ChatData.OwnerID,self.ChatData.SourceType,self.ChatData.ChatType,self.ChatData.Audible,self.ChatData.Position,self.ChatData.Message)

		return output