# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	GroupLimit: "S32"

@dataclass
class GroupData:
	Name: "Variable 1"
	Charter: "Variable 2"
	ShowInList: "BOOL"
	InsigniaID: "LLUUID"
	MembershipFee: "S32"
	OpenEnrollment: "BOOL"
	AllowPublish: "BOOL"
	MaturePublish: "BOOL"


class CreateGroupRequestExtended(Message):

	absolute_id = 4294902189 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.GroupData = GroupData(*((None,)*8))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","signed int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","variable2","unsigned byte","uuid","signed int32","unsigned byte","unsigned byte","unsigned byte",],remaining_bytes)
		self.GroupData = GroupData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: CreateGroupRequestExtended, 
Message Absolute ID: 4294902189
Blocks:
{self.AgentData}
{self.GroupData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","signed int32",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupLimit)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","variable2","unsigned byte","uuid","signed int32","unsigned byte","unsigned byte","unsigned byte",],self.GroupData.Name,self.GroupData.Charter,self.GroupData.ShowInList,self.GroupData.InsigniaID,self.GroupData.MembershipFee,self.GroupData.OpenEnrollment,self.GroupData.AllowPublish,self.GroupData.MaturePublish)

		return output