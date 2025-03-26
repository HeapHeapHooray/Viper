# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class MuteData:
	AgentID: "LLUUID"
	Filename: "Variable 1"


class MuteListUpdate(Message):

	absolute_id = 4294902078 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.MuteData = MuteData(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1",],remaining_bytes)
		self.MuteData = MuteData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: MuteListUpdate, 
Message Absolute ID: 4294902078
Blocks:
{self.MuteData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1",],self.MuteData.AgentID,self.MuteData.Filename)

		return output