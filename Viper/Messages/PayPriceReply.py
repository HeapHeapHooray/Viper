# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ObjectData:
	ObjectID: "LLUUID"
	DefaultPayPrice: "S32"

@dataclass
class ButtonData:
	PayButton: "S32"


class PayPriceReply(Message):

	absolute_id = 4294901922 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ObjectData = ObjectData(*((None,)*2))
		self.ButtonData = [ButtonData(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32",],remaining_bytes)
		self.ObjectData = ObjectData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ButtonData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32",],remaining_bytes)
			self.ButtonData.append(ButtonData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: PayPriceReply, 
Message Absolute ID: 4294901922
Blocks:
{self.ObjectData}
{self.ButtonData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32",],self.ObjectData.ObjectID,self.ObjectData.DefaultPayPrice)

		blocks_count = len(self.ButtonData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["signed int32",],self.ButtonData[i].PayButton)

		return output