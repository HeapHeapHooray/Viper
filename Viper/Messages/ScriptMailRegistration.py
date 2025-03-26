# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	TargetIP: "Variable 1"
	TargetPort: "IPPORT"
	TaskID: "LLUUID"
	Flags: "U32"


class ScriptMailRegistration(Message):

	absolute_id = 4294902178 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = DataBlock(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","unsigned int16","uuid","unsigned int32",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ScriptMailRegistration, 
Message Absolute ID: 4294902178
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","unsigned int16","uuid","unsigned int32",],self.DataBlock.TargetIP,self.DataBlock.TargetPort,self.DataBlock.TaskID,self.DataBlock.Flags)

		return output