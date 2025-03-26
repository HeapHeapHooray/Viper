# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Data:
	Ratio: "U8"


class SetCPURatio(Message):

	absolute_id = 4294902087 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = Data(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
		self.Data = Data(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SetCPURatio, 
Message Absolute ID: 4294902087
Blocks:
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.Data.Ratio)

		return output