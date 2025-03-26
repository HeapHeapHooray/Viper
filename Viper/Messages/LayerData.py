# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class LayerID:
	Type: "U8"

@dataclass
class LayerData:
	Data: "Variable 2"


class LayerData(Message):

	absolute_id = 11 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.LayerID = LayerID(*((None,)*1))
		self.LayerData = LayerData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
		self.LayerID = LayerID(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
		self.LayerData = LayerData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: LayerData, 
Message Absolute ID: 11
Blocks:
{self.LayerID}
{self.LayerData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.LayerID.Type)

		output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.LayerData.Data)

		return output