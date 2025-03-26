# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	GroupID: "LLUUID"
	RequestID: "LLUUID"
	TotalPairs: "U32"

@dataclass
class MemberData:
	RoleID: "LLUUID"
	MemberID: "LLUUID"


class GroupRoleMembersReply(Message):

	absolute_id = 4294902134 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*4))
		self.MemberData = [MemberData(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","unsigned int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.MemberData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
			self.MemberData.append(MemberData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupRoleMembersReply, 
Message Absolute ID: 4294902134
Blocks:
{self.AgentData}
{self.MemberData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","unsigned int32",],self.AgentData.AgentID,self.AgentData.GroupID,self.AgentData.RequestID,self.AgentData.TotalPairs)

		blocks_count = len(self.MemberData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.MemberData[i].RoleID,self.MemberData[i].MemberID)

		return output