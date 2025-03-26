# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ObjectData:
	ObjectID: "LLUUID"


class RequestPayPrice(Message):

	absolute_id = 4294901921 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ObjectData = ObjectData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.ObjectData = ObjectData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RequestPayPrice, 
Message Absolute ID: 4294901921
Blocks:
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.ObjectData.ObjectID)

		return output