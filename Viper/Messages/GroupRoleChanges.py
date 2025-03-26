# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	GroupID: "LLUUID"

@dataclass
class RoleChange:
	RoleID: "LLUUID"
	MemberID: "LLUUID"
	Change: "U32"


class GroupRoleChanges(Message):

	absolute_id = 4294902102 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.RoleChange = [RoleChange(*((None,)*3))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.RoleChange = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32",],remaining_bytes)
			self.RoleChange.append(RoleChange(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupRoleChanges, 
Message Absolute ID: 4294902102
Blocks:
{self.AgentData}
{self.RoleChange}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupID)

		blocks_count = len(self.RoleChange)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32",],self.RoleChange[i].RoleID,self.RoleChange[i].MemberID,self.RoleChange[i].Change)

		return output