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
class TransactionData:
	TransactionID: "LLUUID"
TRANSACTIONDATA = TransactionData


class GroupVoteHistoryRequest(Message):

	absolute_id = 4294902121 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*2))

		self.GroupData = GROUPDATA(*((None,)*1))

		self.TransactionData = TRANSACTIONDATA(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.GroupData = GROUPDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.TransactionData = TRANSACTIONDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupVoteHistoryRequest, Message Absolute ID: 4294902121, Blocks: {self.AgentData},{self.GroupData},{self.TransactionData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.GroupData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.TransactionData.TransactionID)

		return output