# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AssetBlock:
	TransactionID: "LLUUID"
	Type: "S8"
	Tempfile: "BOOL"
	StoreLocal: "BOOL"
	AssetData: "Variable 2"


class AssetUploadRequest(Message):

	absolute_id = 4294902093 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AssetBlock = AssetBlock(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed byte","unsigned byte","unsigned byte","variable2",],remaining_bytes)
		self.AssetBlock = AssetBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AssetUploadRequest, 
Message Absolute ID: 4294902093
Blocks:
{self.AssetBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed byte","unsigned byte","unsigned byte","variable2",],self.AssetBlock.TransactionID,self.AssetBlock.Type,self.AssetBlock.Tempfile,self.AssetBlock.StoreLocal,self.AssetBlock.AssetData)

		return output