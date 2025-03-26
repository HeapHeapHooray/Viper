# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TransferInfo:
	TransferID: "LLUUID"
	ChannelType: "S32"
	TargetType: "S32"
	Status: "S32"
	Size: "S32"
	Params: "Variable 2"


class TransferInfo(Message):

	absolute_id = 4294901914 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TransferInfo = TransferInfo(*((None,)*6))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","signed int32","signed int32","signed int32","variable2",],remaining_bytes)
		self.TransferInfo = TransferInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TransferInfo, 
Message Absolute ID: 4294901914
Blocks:
{self.TransferInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","signed int32","signed int32","signed int32","variable2",],self.TransferInfo.TransferID,self.TransferInfo.ChannelType,self.TransferInfo.TargetType,self.TransferInfo.Status,self.TransferInfo.Size,self.TransferInfo.Params)

		return output