# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class Data:
	ObjectID: "LLUUID"
	Delete: "BOOL"
DATA = Data


class DerezContainer(Message):

	absolute_id = 4294901864 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = DATA(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
		self.Data = DATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: DerezContainer, 
Message Absolute ID: 4294901864
Blocks:
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte",],self.Data.ObjectID,self.Data.Delete)

		return output