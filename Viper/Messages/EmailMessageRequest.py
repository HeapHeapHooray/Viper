# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	ObjectID: "LLUUID"
	FromAddress: "Variable 1"
	Subject: "Variable 1"


class EmailMessageRequest(Message):

	absolute_id = 4294902095 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = DataBlock(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","variable1",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: EmailMessageRequest, 
Message Absolute ID: 4294902095
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","variable1",],self.DataBlock.ObjectID,self.DataBlock.FromAddress,self.DataBlock.Subject)

		return output