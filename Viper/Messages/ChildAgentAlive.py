# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	RegionHandle: "U64"
	ViewerCircuitCode: "U32"
	AgentID: "LLUUID"
	SessionID: "LLUUID"


class ChildAgentAlive(Message):

	absolute_id = 26 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","unsigned int32","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ChildAgentAlive, 
Message Absolute ID: 26
Blocks:
{self.AgentData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","unsigned int32","uuid","uuid",],self.AgentData.RegionHandle,self.AgentData.ViewerCircuitCode,self.AgentData.AgentID,self.AgentData.SessionID)

		return output