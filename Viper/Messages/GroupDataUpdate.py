# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentGroupData:
	AgentID: "LLUUID"
	GroupID: "LLUUID"
	AgentPowers: "U64"
	GroupTitle: "Variable 1"


class GroupDataUpdate(Message):

	absolute_id = 4294902148 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentGroupData = [AgentGroupData(*((None,)*4))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AgentGroupData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int64","variable1",],remaining_bytes)
			self.AgentGroupData.append(AgentGroupData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupDataUpdate, 
Message Absolute ID: 4294902148
Blocks:
{self.AgentGroupData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.AgentGroupData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int64","variable1",],self.AgentGroupData[i].AgentID,self.AgentGroupData[i].GroupID,self.AgentGroupData[i].AgentPowers,self.AgentGroupData[i].GroupTitle)

		return output