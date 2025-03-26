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
	Name: "Variable 1"
	Charter: "Variable 2"
	ShowInList: "BOOL"
	MemberTitle: "Variable 1"
	PowersMask: "U64"
	InsigniaID: "LLUUID"
	FounderID: "LLUUID"
	MembershipFee: "S32"
	OpenEnrollment: "BOOL"
	Money: "S32"
	GroupMembershipCount: "S32"
	GroupRolesCount: "S32"
	AllowPublish: "BOOL"
	MaturePublish: "BOOL"
	OwnerRole: "LLUUID"


class GroupProfileReply(Message):

	absolute_id = 4294902112 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.GroupData = GroupData(*((None,)*16))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","variable2","unsigned byte","variable1","unsigned int64","uuid","uuid","signed int32","unsigned byte","signed int32","signed int32","signed int32","unsigned byte","unsigned byte","uuid",],remaining_bytes)
		self.GroupData = GroupData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupProfileReply, 
Message Absolute ID: 4294902112
Blocks:
{self.AgentData}
{self.GroupData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","variable2","unsigned byte","variable1","unsigned int64","uuid","uuid","signed int32","unsigned byte","signed int32","signed int32","signed int32","unsigned byte","unsigned byte","uuid",],self.GroupData.GroupID,self.GroupData.Name,self.GroupData.Charter,self.GroupData.ShowInList,self.GroupData.MemberTitle,self.GroupData.PowersMask,self.GroupData.InsigniaID,self.GroupData.FounderID,self.GroupData.MembershipFee,self.GroupData.OpenEnrollment,self.GroupData.Money,self.GroupData.GroupMembershipCount,self.GroupData.GroupRolesCount,self.GroupData.AllowPublish,self.GroupData.MaturePublish,self.GroupData.OwnerRole)

		return output