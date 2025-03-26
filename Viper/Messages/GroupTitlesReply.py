# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	GroupID: "LLUUID"
	RequestID: "LLUUID"

@dataclass
class GroupData:
	Title: "Variable 1"
	RoleID: "LLUUID"
	Selected: "BOOL"


class GroupTitlesReply(Message):

	absolute_id = 4294902136 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.GroupData = [GroupData(*((None,)*3))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.GroupData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","uuid","unsigned byte",],remaining_bytes)
			self.GroupData.append(GroupData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupTitlesReply, 
Message Absolute ID: 4294902136
Blocks:
{self.AgentData}
{self.GroupData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.GroupID,self.AgentData.RequestID)

		blocks_count = len(self.GroupData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable1","uuid","unsigned byte",],self.GroupData[i].Title,self.GroupData[i].RoleID,self.GroupData[i].Selected)

		return output