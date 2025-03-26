# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	AvatarID: "LLUUID"

@dataclass
class GroupData:
	GroupPowers: "U64"
	AcceptNotices: "BOOL"
	GroupTitle: "Variable 1"
	GroupID: "LLUUID"
	GroupName: "Variable 1"
	GroupInsigniaID: "LLUUID"

@dataclass
class NewGroupData:
	ListInProfile: "BOOL"


class AvatarGroupsReply(Message):

	absolute_id = 4294901933 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.GroupData = [GroupData(*((None,)*6))]
		self.NewGroupData = NewGroupData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.GroupData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","unsigned byte","variable1","uuid","variable1","uuid",],remaining_bytes)
			self.GroupData.append(GroupData(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
		self.NewGroupData = NewGroupData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarGroupsReply, 
Message Absolute ID: 4294901933
Blocks:
{self.AgentData}
{self.GroupData}
{self.NewGroupData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.AvatarID)

		blocks_count = len(self.GroupData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","unsigned byte","variable1","uuid","variable1","uuid",],self.GroupData[i].GroupPowers,self.GroupData[i].AcceptNotices,self.GroupData[i].GroupTitle,self.GroupData[i].GroupID,self.GroupData[i].GroupName,self.GroupData[i].GroupInsigniaID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.NewGroupData.ListInProfile)

		return output