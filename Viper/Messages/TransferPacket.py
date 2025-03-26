# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TransferData:
	TransferID: "LLUUID"
	ChannelType: "S32"
	Packet: "S32"
	Status: "S32"
	Data: "Variable 2"


class TransferPacket(Message):

	absolute_id = 17 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TransferData = TransferData(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","signed int32","signed int32","variable2",],remaining_bytes)
		self.TransferData = TransferData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TransferPacket, 
Message Absolute ID: 17
Blocks:
{self.TransferData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","signed int32","signed int32","variable2",],self.TransferData.TransferID,self.TransferData.ChannelType,self.TransferData.Packet,self.TransferData.Status,self.TransferData.Data)

		return output