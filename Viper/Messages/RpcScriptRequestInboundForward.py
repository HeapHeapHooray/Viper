# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	RPCServerIP: "IPADDR"
	RPCServerPort: "IPPORT"
	TaskID: "LLUUID"
	ItemID: "LLUUID"
	ChannelID: "LLUUID"
	IntValue: "U32"
	StringValue: "Variable 2"


class RpcScriptRequestInboundForward(Message):

	absolute_id = 4294902176 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = DataBlock(*((None,)*7))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int16","uuid","uuid","uuid","unsigned int32","variable2",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RpcScriptRequestInboundForward, 
Message Absolute ID: 4294902176
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int16","uuid","uuid","uuid","unsigned int32","variable2",],self.DataBlock.RPCServerIP,self.DataBlock.RPCServerPort,self.DataBlock.TaskID,self.DataBlock.ItemID,self.DataBlock.ChannelID,self.DataBlock.IntValue,self.DataBlock.StringValue)

		return output