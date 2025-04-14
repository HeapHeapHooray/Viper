# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class XferID:
	ID: "U64"
	Result: "S32"
XFERID = XferID


class AbortXfer(Message):

	absolute_id = 4294901917 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.XferID = XFERID(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","signed int32",],remaining_bytes)
		self.XferID = XFERID(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AbortXfer, 
Message Absolute ID: 4294901917
Blocks:
{self.XferID}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","signed int32",],self.XferID.ID,self.XferID.Result)

		return output