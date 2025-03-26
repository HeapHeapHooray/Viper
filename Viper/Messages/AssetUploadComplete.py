# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AssetBlock:
	UUID: "LLUUID"
	Type: "S8"
	Success: "BOOL"


class AssetUploadComplete(Message):

	absolute_id = 4294902094 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AssetBlock = AssetBlock(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed byte","unsigned byte",],remaining_bytes)
		self.AssetBlock = AssetBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AssetUploadComplete, 
Message Absolute ID: 4294902094
Blocks:
{self.AssetBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed byte","unsigned byte",],self.AssetBlock.UUID,self.AssetBlock.Type,self.AssetBlock.Success)

		return output