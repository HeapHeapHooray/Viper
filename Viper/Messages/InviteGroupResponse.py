# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class InviteData:
	AgentID: "LLUUID"
	InviteeID: "LLUUID"
	GroupID: "LLUUID"
	RoleID: "LLUUID"
	MembershipFee: "S32"

@dataclass
class GroupData:
	GroupLimit: "S32"


class InviteGroupResponse(Message):

	absolute_id = 4294902110 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.InviteData = InviteData(*((None,)*5))
		self.GroupData = GroupData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","uuid","signed int32",],remaining_bytes)
		self.InviteData = InviteData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32",],remaining_bytes)
		self.GroupData = GroupData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: InviteGroupResponse, 
Message Absolute ID: 4294902110
Blocks:
{self.InviteData}
{self.GroupData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","uuid","signed int32",],self.InviteData.AgentID,self.InviteData.InviteeID,self.InviteData.GroupID,self.InviteData.RoleID,self.InviteData.MembershipFee)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32",],self.GroupData.GroupLimit)

		return output