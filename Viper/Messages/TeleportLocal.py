# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Info:
	AgentID: "LLUUID"
	LocationID: "U32"
	Position: "LLVector3"
	LookAt: "LLVector3"
	TeleportFlags: "U32"


class TeleportLocal(Message):

	absolute_id = 4294901824 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Info = Info(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32","vector3","vector3","unsigned int32",],remaining_bytes)
		self.Info = Info(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TeleportLocal, 
Message Absolute ID: 4294901824
Blocks:
{self.Info}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32","vector3","vector3","unsigned int32",],self.Info.AgentID,self.Info.LocationID,self.Info.Position,self.Info.LookAt,self.Info.TeleportFlags)

		return output