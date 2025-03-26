# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class QueryData:
	QueryID: "LLUUID"
	AssetID: "LLUUID"
	IsReadable: "BOOL"


class InventoryAssetResponse(Message):

	absolute_id = 4294902043 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.QueryData = QueryData(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte",],remaining_bytes)
		self.QueryData = QueryData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: InventoryAssetResponse, 
Message Absolute ID: 4294902043
Blocks:
{self.QueryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte",],self.QueryData.QueryID,self.QueryData.AssetID,self.QueryData.IsReadable)

		return output