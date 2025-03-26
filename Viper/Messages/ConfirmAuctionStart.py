# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AuctionData:
	ParcelID: "LLUUID"
	AuctionID: "U32"


class ConfirmAuctionStart(Message):

	absolute_id = 4294901990 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AuctionData = AuctionData(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32",],remaining_bytes)
		self.AuctionData = AuctionData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ConfirmAuctionStart, 
Message Absolute ID: 4294901990
Blocks:
{self.AuctionData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32",],self.AuctionData.ParcelID,self.AuctionData.AuctionID)

		return output