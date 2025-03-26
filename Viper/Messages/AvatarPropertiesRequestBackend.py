# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	AvatarID: "LLUUID"
	GodLevel: "U8"
	WebProfilesDisabled: "BOOL"


class AvatarPropertiesRequestBackend(Message):

	absolute_id = 4294901930 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte","unsigned byte",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarPropertiesRequestBackend, 
Message Absolute ID: 4294901930
Blocks:
{self.AgentData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte","unsigned byte",],self.AgentData.AgentID,self.AgentData.AvatarID,self.AgentData.GodLevel,self.AgentData.WebProfilesDisabled)

		return output