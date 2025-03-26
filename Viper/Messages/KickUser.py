# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TargetBlock:
	TargetIP: "IPADDR"
	TargetPort: "IPPORT"

@dataclass
class UserInfo:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	Reason: "Variable 2"


class KickUser(Message):

	absolute_id = 4294901923 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TargetBlock = TargetBlock(*((None,)*2))
		self.UserInfo = UserInfo(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int16",],remaining_bytes)
		self.TargetBlock = TargetBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","variable2",],remaining_bytes)
		self.UserInfo = UserInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: KickUser, 
Message Absolute ID: 4294901923
Blocks:
{self.TargetBlock}
{self.UserInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int16",],self.TargetBlock.TargetIP,self.TargetBlock.TargetPort)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","variable2",],self.UserInfo.AgentID,self.UserInfo.SessionID,self.UserInfo.Reason)

		return output