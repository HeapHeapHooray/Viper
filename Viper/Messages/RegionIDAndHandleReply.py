# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class ReplyBlock:
	RegionID: "LLUUID"
	RegionHandle: "U64"
REPLYBLOCK = ReplyBlock


class RegionIDAndHandleReply(Message):

	absolute_id = 4294902070 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ReplyBlock = REPLYBLOCK(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int64",],remaining_bytes)
		self.ReplyBlock = REPLYBLOCK(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RegionIDAndHandleReply, 
Message Absolute ID: 4294902070
Blocks:
{self.ReplyBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int64",],self.ReplyBlock.RegionID,self.ReplyBlock.RegionHandle)

		return output