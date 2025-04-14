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
	Success: "BOOL"
GROUPDATA = GroupData


class JoinGroupReply(Message):

	absolute_id = 4294902104 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*1))

		self.GroupData = GROUPDATA(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
		self.GroupData = GROUPDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: JoinGroupReply, Message Absolute ID: 4294902104, Blocks: {self.AgentData},{self.GroupData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte",],self.GroupData.GroupID,self.GroupData.Success)

		return output