# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ParcelData:
	SequenceID: "S32"
	Data: "Variable 2"


class ParcelOverlay(Message):

	absolute_id = 4294901956 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ParcelData = ParcelData(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","variable2",],remaining_bytes)
		self.ParcelData = ParcelData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelOverlay, 
Message Absolute ID: 4294901956
Blocks:
{self.ParcelData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","variable2",],self.ParcelData.SequenceID,self.ParcelData.Data)

		return output