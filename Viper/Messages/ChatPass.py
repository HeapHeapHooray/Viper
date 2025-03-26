# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ChatData:
	Channel: "S32"
	Position: "LLVector3"
	ID: "LLUUID"
	OwnerID: "LLUUID"
	Name: "Variable 1"
	SourceType: "U8"
	Type: "U8"
	Radius: "F32"
	SimAccess: "U8"
	Message: "Variable 2"


class ChatPass(Message):

	absolute_id = 4294901999 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ChatData = ChatData(*((None,)*10))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","vector3","uuid","uuid","variable1","unsigned byte","unsigned byte","float","unsigned byte","variable2",],remaining_bytes)
		self.ChatData = ChatData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ChatPass, 
Message Absolute ID: 4294901999
Blocks:
{self.ChatData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","vector3","uuid","uuid","variable1","unsigned byte","unsigned byte","float","unsigned byte","variable2",],self.ChatData.Channel,self.ChatData.Position,self.ChatData.ID,self.ChatData.OwnerID,self.ChatData.Name,self.ChatData.SourceType,self.ChatData.Type,self.ChatData.Radius,self.ChatData.SimAccess,self.ChatData.Message)

		return output