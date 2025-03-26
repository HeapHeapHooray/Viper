# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"

@dataclass
class UserData:
	IMViaEMail: "BOOL"
	DirectoryVisibility: "Variable 1"
	EMail: "Variable 2"


class UserInfoReply(Message):

	absolute_id = 4294902160 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.UserData = UserData(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","variable1","variable2",],remaining_bytes)
		self.UserData = UserData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: UserInfoReply, 
Message Absolute ID: 4294902160
Blocks:
{self.AgentData}
{self.UserData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","variable1","variable2",],self.UserData.IMViaEMail,self.UserData.DirectoryVisibility,self.UserData.EMail)

		return output