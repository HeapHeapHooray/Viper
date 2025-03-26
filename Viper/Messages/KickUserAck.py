# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class UserInfo:
	SessionID: "LLUUID"
	Flags: "U32"


class KickUserAck(Message):

	absolute_id = 4294901924 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.UserInfo = UserInfo(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32",],remaining_bytes)
		self.UserInfo = UserInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: KickUserAck, 
Message Absolute ID: 4294901924
Blocks:
{self.UserInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32",],self.UserInfo.SessionID,self.UserInfo.Flags)

		return output