# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class NetBlock:
	Port: "IPPORT"


class NetTest(Message):

	absolute_id = 4294902086 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.NetBlock = NetBlock(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int16",],remaining_bytes)
		self.NetBlock = NetBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: NetTest, 
Message Absolute ID: 4294902086
Blocks:
{self.NetBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int16",],self.NetBlock.Port)

		return output