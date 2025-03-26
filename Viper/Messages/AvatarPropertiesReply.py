# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	AvatarID: "LLUUID"

@dataclass
class PropertiesData:
	ImageID: "LLUUID"
	FLImageID: "LLUUID"
	PartnerID: "LLUUID"
	AboutText: "Variable 2"
	FLAboutText: "Variable 1"
	BornOn: "Variable 1"
	ProfileURL: "Variable 1"
	CharterMember: "Variable 1"
	Flags: "U32"


class AvatarPropertiesReply(Message):

	absolute_id = 4294901931 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.PropertiesData = PropertiesData(*((None,)*9))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","variable2","variable1","variable1","variable1","variable1","unsigned int32",],remaining_bytes)
		self.PropertiesData = PropertiesData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarPropertiesReply, 
Message Absolute ID: 4294901931
Blocks:
{self.AgentData}
{self.PropertiesData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.AvatarID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","variable2","variable1","variable1","variable1","variable1","unsigned int32",],self.PropertiesData.ImageID,self.PropertiesData.FLImageID,self.PropertiesData.PartnerID,self.PropertiesData.AboutText,self.PropertiesData.FLAboutText,self.PropertiesData.BornOn,self.PropertiesData.ProfileURL,self.PropertiesData.CharterMember,self.PropertiesData.Flags)

		return output