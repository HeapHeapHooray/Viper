# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	AssetID: "LLUUID"
	PosGlobal: "LLVector3d"
	To: "Variable 1"
	From: "Variable 1"
	Name: "Variable 1"
	Subject: "Variable 1"
	Msg: "Variable 2"
	AllowPublish: "BOOL"
	MaturePublish: "BOOL"


class SendPostcard(Message):

	absolute_id = 4294902172 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*11))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","vector3d","variable1","variable1","variable1","variable1","variable2","unsigned byte","unsigned byte",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SendPostcard, 
Message Absolute ID: 4294902172
Blocks:
{self.AgentData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","vector3d","variable1","variable1","variable1","variable1","variable2","unsigned byte","unsigned byte",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.AssetID,self.AgentData.PosGlobal,self.AgentData.To,self.AgentData.From,self.AgentData.Name,self.AgentData.Subject,self.AgentData.Msg,self.AgentData.AllowPublish,self.AgentData.MaturePublish)

		return output