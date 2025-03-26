# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ImageID:
	ID: "LLUUID"


class ImageNotInDatabase(Message):

	absolute_id = 4294901846 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ImageID = ImageID(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.ImageID = ImageID(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ImageNotInDatabase, 
Message Absolute ID: 4294901846
Blocks:
{self.ImageID}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.ImageID.ID)

		return output