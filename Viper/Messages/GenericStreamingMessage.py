# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class MethodData:
	Method: "U16"

@dataclass
class DataBlock:
	Data: "Variable 2"


class GenericStreamingMessage(Message):

	absolute_id = 31 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.MethodData = MethodData(*((None,)*1))
		self.DataBlock = DataBlock(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int16",],remaining_bytes)
		self.MethodData = MethodData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: GenericStreamingMessage, 
Message Absolute ID: 31
Blocks:
{self.MethodData}
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int16",],self.MethodData.Method)

		output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.DataBlock.Data)

		return output