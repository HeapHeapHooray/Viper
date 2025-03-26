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
	WantToMask: "U32"
	WantToText: "Variable 1"
	SkillsMask: "U32"
	SkillsText: "Variable 1"
	LanguagesText: "Variable 1"


class AvatarInterestsUpdate(Message):

	absolute_id = 4294901935 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.PropertiesData = PropertiesData(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","variable1","unsigned int32","variable1","variable1",],remaining_bytes)
		self.PropertiesData = PropertiesData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarInterestsUpdate, 
Message Absolute ID: 4294901935
Blocks:
{self.AgentData}
{self.PropertiesData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","variable1","unsigned int32","variable1","variable1",],self.PropertiesData.WantToMask,self.PropertiesData.WantToText,self.PropertiesData.SkillsMask,self.PropertiesData.SkillsText,self.PropertiesData.LanguagesText)

		return output