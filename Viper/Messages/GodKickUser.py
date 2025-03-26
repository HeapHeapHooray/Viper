# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class UserInfo:
	GodID: "LLUUID"
	GodSessionID: "LLUUID"
	AgentID: "LLUUID"
	KickFlags: "U32"
	Reason: "Variable 2"


class GodKickUser(Message):

	absolute_id = 4294901925 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.UserInfo = UserInfo(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","unsigned int32","variable2",],remaining_bytes)
		self.UserInfo = UserInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: GodKickUser, 
Message Absolute ID: 4294901925
Blocks:
{self.UserInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","unsigned int32","variable2",],self.UserInfo.GodID,self.UserInfo.GodSessionID,self.UserInfo.AgentID,self.UserInfo.KickFlags,self.UserInfo.Reason)

		return output