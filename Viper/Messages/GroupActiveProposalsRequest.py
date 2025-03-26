# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class GroupData:
	GroupID: "LLUUID"

@dataclass
class TransactionData:
	TransactionID: "LLUUID"


class GroupActiveProposalsRequest(Message):

	absolute_id = 4294902119 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.GroupData = GroupData(*((None,)*1))
		self.TransactionData = TransactionData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.GroupData = GroupData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.TransactionData = TransactionData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupActiveProposalsRequest, 
Message Absolute ID: 4294902119
Blocks:
{self.AgentData}
{self.GroupData}
{self.TransactionData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.GroupData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.TransactionData.TransactionID)

		return output