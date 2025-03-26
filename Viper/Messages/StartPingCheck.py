# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class PingID:
	PingID: "U8"
	OldestUnacked: "U32"


class StartPingCheck(Message):

	absolute_id = 1 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.PingID = PingID(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned int32",],remaining_bytes)
		self.PingID = PingID(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: StartPingCheck, 
Message Absolute ID: 1
Blocks:
{self.PingID}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned int32",],self.PingID.PingID,self.PingID.OldestUnacked)

		return output