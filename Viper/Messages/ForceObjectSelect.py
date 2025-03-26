# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Header:
	ResetList: "BOOL"

@dataclass
class Data:
	LocalID: "U32"


class ForceObjectSelect(Message):

	absolute_id = 4294901965 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Header = Header(*((None,)*1))
		self.Data = [Data(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
		self.Header = Header(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Data = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
			self.Data.append(Data(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ForceObjectSelect, 
Message Absolute ID: 4294901965
Blocks:
{self.Header}
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.Header.ResetList)

		blocks_count = len(self.Data)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.Data[i].LocalID)

		return output