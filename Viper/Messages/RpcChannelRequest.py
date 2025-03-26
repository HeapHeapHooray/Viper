# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	GridX: "U32"
	GridY: "U32"
	TaskID: "LLUUID"
	ItemID: "LLUUID"


class RpcChannelRequest(Message):

	absolute_id = 4294902173 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = DataBlock(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","uuid","uuid",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RpcChannelRequest, 
Message Absolute ID: 4294902173
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","uuid","uuid",],self.DataBlock.GridX,self.DataBlock.GridY,self.DataBlock.TaskID,self.DataBlock.ItemID)

		return output