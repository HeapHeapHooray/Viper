# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Script:
	ObjectID: "LLUUID"
	ItemID: "LLUUID"


class GetScriptRunning(Message):

	absolute_id = 4294902003 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Script = Script(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.Script = Script(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: GetScriptRunning, 
Message Absolute ID: 4294902003
Blocks:
{self.Script}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.Script.ObjectID,self.Script.ItemID)

		return output