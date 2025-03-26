# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	MediaURL: "Variable 1"
	MediaID: "LLUUID"
	MediaAutoScale: "U8"

@dataclass
class DataBlockExtended:
	MediaType: "Variable 1"
	MediaDesc: "Variable 1"
	MediaWidth: "S32"
	MediaHeight: "S32"
	MediaLoop: "U8"


class ParcelMediaUpdate(Message):

	absolute_id = 4294902180 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = DataBlock(*((None,)*3))
		self.DataBlockExtended = DataBlockExtended(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","uuid","unsigned byte",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","variable1","signed int32","signed int32","unsigned byte",],remaining_bytes)
		self.DataBlockExtended = DataBlockExtended(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelMediaUpdate, 
Message Absolute ID: 4294902180
Blocks:
{self.DataBlock}
{self.DataBlockExtended}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","uuid","unsigned byte",],self.DataBlock.MediaURL,self.DataBlock.MediaID,self.DataBlock.MediaAutoScale)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","variable1","signed int32","signed int32","unsigned byte",],self.DataBlockExtended.MediaType,self.DataBlockExtended.MediaDesc,self.DataBlockExtended.MediaWidth,self.DataBlockExtended.MediaHeight,self.DataBlockExtended.MediaLoop)

		return output