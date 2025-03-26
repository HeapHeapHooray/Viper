# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"

@dataclass
class GroupData:
	GroupID: "LLUUID"
	RequestID: "LLUUID"
	MemberCount: "S32"

@dataclass
class MemberData:
	AgentID: "LLUUID"
	Contribution: "S32"
	OnlineStatus: "Variable 1"
	AgentPowers: "U64"
	Title: "Variable 1"
	IsOwner: "BOOL"


class GroupMembersReply(Message):

	absolute_id = 4294902127 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.GroupData = GroupData(*((None,)*3))
		self.MemberData = [MemberData(*((None,)*6))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","signed int32",],remaining_bytes)
		self.GroupData = GroupData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.MemberData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","variable1","unsigned int64","variable1","unsigned byte",],remaining_bytes)
			self.MemberData.append(MemberData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupMembersReply, 
Message Absolute ID: 4294902127
Blocks:
{self.AgentData}
{self.GroupData}
{self.MemberData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","signed int32",],self.GroupData.GroupID,self.GroupData.RequestID,self.GroupData.MemberCount)

		blocks_count = len(self.MemberData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","variable1","unsigned int64","variable1","unsigned byte",],self.MemberData[i].AgentID,self.MemberData[i].Contribution,self.MemberData[i].OnlineStatus,self.MemberData[i].AgentPowers,self.MemberData[i].Title,self.MemberData[i].IsOwner)

		return output