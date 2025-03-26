# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	From: "Variable 1"
	To: "LLUUID"
	Subject: "Variable 1"
	Body: "Variable 2"


class InternalScriptMail(Message):

	absolute_id = 65296 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = DataBlock(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","uuid","variable1","variable2",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: InternalScriptMail, 
Message Absolute ID: 65296
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","uuid","variable1","variable2",],self.DataBlock.From,self.DataBlock.To,self.DataBlock.Subject,self.DataBlock.Body)

		return output