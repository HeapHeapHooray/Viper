# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class GroupData:
	GroupID: "LLUUID"
GROUPDATA = GroupData

@dataclass
class EjectData:
	Success: "BOOL"
EJECTDATA = EjectData


class EjectGroupMemberReply(Message):

	absolute_id = 4294902106 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*1))

		self.GroupData = GROUPDATA(*((None,)*1))

		self.EjectData = EJECTDATA(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.GroupData = GROUPDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
		self.EjectData = EJECTDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: EjectGroupMemberReply, Message Absolute ID: 4294902106, Blocks: {self.AgentData},{self.GroupData},{self.EjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.GroupData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.EjectData.Success)

		return output