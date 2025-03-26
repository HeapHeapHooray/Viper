# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Packets:
	ID: "U32"


class PacketAck(Message):

	absolute_id = 4294967291 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Packets = [Packets(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Packets = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
			self.Packets.append(Packets(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: PacketAck, 
Message Absolute ID: 4294967291
Blocks:
{self.Packets}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.Packets)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.Packets[i].ID)

		return output