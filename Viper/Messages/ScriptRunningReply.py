# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Script:
	ObjectID: "LLUUID"
	ItemID: "LLUUID"
	Running: "BOOL"


class ScriptRunningReply(Message):

	absolute_id = 4294902004 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Script = Script(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte",],remaining_bytes)
		self.Script = Script(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ScriptRunningReply, 
Message Absolute ID: 4294902004
Blocks:
{self.Script}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte",],self.Script.ObjectID,self.Script.ItemID,self.Script.Running)

		return output