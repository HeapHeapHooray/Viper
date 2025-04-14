# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class GroupData:
	GroupID: "LLUUID"
GROUPDATA = GroupData

@dataclass
class InviteData:
	InviteeID: "LLUUID"
	RoleID: "LLUUID"
INVITEDATA = InviteData


class InviteGroupRequest(Message):

	absolute_id = 4294902109 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*2))
		self.GroupData = GROUPDATA(*((None,)*1))
		self.InviteData = [INVITEDATA(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.GroupData = GROUPDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.InviteData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
			self.InviteData.append(INVITEDATA(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: InviteGroupRequest, 
Message Absolute ID: 4294902109
Blocks:
{self.AgentData}
{self.GroupData}
{self.InviteData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.GroupData.GroupID)

		blocks_count = len(self.InviteData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.InviteData[i].InviteeID,self.InviteData[i].RoleID)

		return output