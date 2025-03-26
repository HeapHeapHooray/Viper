# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TargetBlock:
	GridX: "U32"
	GridY: "U32"

@dataclass
class DataBlock:
	TaskID: "LLUUID"
	ItemID: "LLUUID"
	ChannelID: "LLUUID"
	IntValue: "U32"
	StringValue: "Variable 2"


class RpcScriptRequestInbound(Message):

	absolute_id = 4294902175 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TargetBlock = TargetBlock(*((None,)*2))
		self.DataBlock = DataBlock(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32",],remaining_bytes)
		self.TargetBlock = TargetBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","unsigned int32","variable2",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RpcScriptRequestInbound, 
Message Absolute ID: 4294902175
Blocks:
{self.TargetBlock}
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32",],self.TargetBlock.GridX,self.TargetBlock.GridY)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","unsigned int32","variable2",],self.DataBlock.TaskID,self.DataBlock.ItemID,self.DataBlock.ChannelID,self.DataBlock.IntValue,self.DataBlock.StringValue)

		return output