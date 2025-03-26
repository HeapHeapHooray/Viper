# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class CommandBlock:
	Flags: "U32"
	Command: "U32"
	Time: "F32"


class ParcelMediaCommandMessage(Message):

	absolute_id = 4294902179 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.CommandBlock = CommandBlock(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","float",],remaining_bytes)
		self.CommandBlock = CommandBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelMediaCommandMessage, 
Message Absolute ID: 4294902179
Blocks:
{self.CommandBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","float",],self.CommandBlock.Flags,self.CommandBlock.Command,self.CommandBlock.Time)

		return output