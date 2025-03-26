# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	FirstName: "Variable 1"
	LastName: "Variable 1"
	GroupTitle: "Variable 1"
	ActiveGroupID: "LLUUID"
	GroupPowers: "U64"
	GroupName: "Variable 1"


class AgentDataUpdate(Message):

	absolute_id = 4294902147 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*7))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","variable1","variable1","uuid","unsigned int64","variable1",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AgentDataUpdate, 
Message Absolute ID: 4294902147
Blocks:
{self.AgentData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","variable1","variable1","uuid","unsigned int64","variable1",],self.AgentData.AgentID,self.AgentData.FirstName,self.AgentData.LastName,self.AgentData.GroupTitle,self.AgentData.ActiveGroupID,self.AgentData.GroupPowers,self.AgentData.GroupName)

		return output