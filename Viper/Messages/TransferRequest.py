# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TransferInfo:
	TransferID: "LLUUID"
	ChannelType: "S32"
	SourceType: "S32"
	Priority: "F32"
	Params: "Variable 2"


class TransferRequest(Message):

	absolute_id = 4294901913 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TransferInfo = TransferInfo(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","signed int32","float","variable2",],remaining_bytes)
		self.TransferInfo = TransferInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TransferRequest, 
Message Absolute ID: 4294901913
Blocks:
{self.TransferInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","signed int32","float","variable2",],self.TransferInfo.TransferID,self.TransferInfo.ChannelType,self.TransferInfo.SourceType,self.TransferInfo.Priority,self.TransferInfo.Params)

		return output