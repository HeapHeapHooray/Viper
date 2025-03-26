# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ImageID:
	ID: "LLUUID"
	Codec: "U8"
	Size: "U32"
	Packets: "U16"

@dataclass
class ImageData:
	Data: "Variable 2"


class ImageData(Message):

	absolute_id = 9 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ImageID = ImageID(*((None,)*4))
		self.ImageData = ImageData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte","unsigned int32","unsigned int16",],remaining_bytes)
		self.ImageID = ImageID(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
		self.ImageData = ImageData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ImageData, 
Message Absolute ID: 9
Blocks:
{self.ImageID}
{self.ImageData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte","unsigned int32","unsigned int16",],self.ImageID.ID,self.ImageID.Codec,self.ImageID.Size,self.ImageID.Packets)

		output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.ImageData.Data)

		return output