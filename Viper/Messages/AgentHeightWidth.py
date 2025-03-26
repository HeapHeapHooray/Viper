# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	CircuitCode: "U32"

@dataclass
class HeightWidthBlock:
	GenCounter: "U32"
	Height: "U16"
	Width: "U16"


class AgentHeightWidth(Message):

	absolute_id = 4294901843 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.HeightWidthBlock = HeightWidthBlock(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int16","unsigned int16",],remaining_bytes)
		self.HeightWidthBlock = HeightWidthBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AgentHeightWidth, 
Message Absolute ID: 4294901843
Blocks:
{self.AgentData}
{self.HeightWidthBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.CircuitCode)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int16","unsigned int16",],self.HeightWidthBlock.GenCounter,self.HeightWidthBlock.Height,self.HeightWidthBlock.Width)

		return output