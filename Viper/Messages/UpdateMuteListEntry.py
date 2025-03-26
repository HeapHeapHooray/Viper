# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class MuteData:
	MuteID: "LLUUID"
	MuteName: "Variable 1"
	MuteType: "S32"
	MuteFlags: "U32"


class UpdateMuteListEntry(Message):

	absolute_id = 4294902023 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.MuteData = MuteData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","signed int32","unsigned int32",],remaining_bytes)
		self.MuteData = MuteData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: UpdateMuteListEntry, 
Message Absolute ID: 4294902023
Blocks:
{self.AgentData}
{self.MuteData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","signed int32","unsigned int32",],self.MuteData.MuteID,self.MuteData.MuteName,self.MuteData.MuteType,self.MuteData.MuteFlags)

		return output