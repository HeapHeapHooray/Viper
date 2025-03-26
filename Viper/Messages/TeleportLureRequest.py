# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Info:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	LureID: "LLUUID"
	TeleportFlags: "U32"


class TeleportLureRequest(Message):

	absolute_id = 4294901831 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Info = Info(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","unsigned int32",],remaining_bytes)
		self.Info = Info(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TeleportLureRequest, 
Message Absolute ID: 4294901831
Blocks:
{self.Info}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","unsigned int32",],self.Info.AgentID,self.Info.SessionID,self.Info.LureID,self.Info.TeleportFlags)

		return output