# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TransferInfo:
	TransferID: "LLUUID"
	ChannelType: "S32"


class TransferAbort(Message):

	absolute_id = 4294901915 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TransferInfo = TransferInfo(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32",],remaining_bytes)
		self.TransferInfo = TransferInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TransferAbort, 
Message Absolute ID: 4294901915
Blocks:
{self.TransferInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32",],self.TransferInfo.TransferID,self.TransferInfo.ChannelType)

		return output