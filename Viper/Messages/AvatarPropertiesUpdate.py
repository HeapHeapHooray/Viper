# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class PropertiesData:
	ImageID: "LLUUID"
	FLImageID: "LLUUID"
	AboutText: "Variable 2"
	FLAboutText: "Variable 1"
	AllowPublish: "BOOL"
	MaturePublish: "BOOL"
	ProfileURL: "Variable 1"


class AvatarPropertiesUpdate(Message):

	absolute_id = 4294901934 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.PropertiesData = PropertiesData(*((None,)*7))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","variable2","variable1","unsigned byte","unsigned byte","variable1",],remaining_bytes)
		self.PropertiesData = PropertiesData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarPropertiesUpdate, 
Message Absolute ID: 4294901934
Blocks:
{self.AgentData}
{self.PropertiesData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","variable2","variable1","unsigned byte","unsigned byte","variable1",],self.PropertiesData.ImageID,self.PropertiesData.FLImageID,self.PropertiesData.AboutText,self.PropertiesData.FLAboutText,self.PropertiesData.AllowPublish,self.PropertiesData.MaturePublish,self.PropertiesData.ProfileURL)

		return output