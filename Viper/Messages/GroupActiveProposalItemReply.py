# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	GroupID: "LLUUID"

@dataclass
class TransactionData:
	TransactionID: "LLUUID"
	TotalNumItems: "U32"

@dataclass
class ProposalData:
	VoteID: "LLUUID"
	VoteInitiator: "LLUUID"
	TerseDateID: "Variable 1"
	StartDateTime: "Variable 1"
	EndDateTime: "Variable 1"
	AlreadyVoted: "BOOL"
	VoteCast: "Variable 1"
	Majority: "F32"
	Quorum: "S32"
	ProposalText: "Variable 1"


class GroupActiveProposalItemReply(Message):

	absolute_id = 4294902120 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.TransactionData = TransactionData(*((None,)*2))
		self.ProposalData = [ProposalData(*((None,)*10))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32",],remaining_bytes)
		self.TransactionData = TransactionData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ProposalData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","variable1","variable1","variable1","unsigned byte","variable1","float","signed int32","variable1",],remaining_bytes)
			self.ProposalData.append(ProposalData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupActiveProposalItemReply, 
Message Absolute ID: 4294902120
Blocks:
{self.AgentData}
{self.TransactionData}
{self.ProposalData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32",],self.TransactionData.TransactionID,self.TransactionData.TotalNumItems)

		blocks_count = len(self.ProposalData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","variable1","variable1","variable1","unsigned byte","variable1","float","signed int32","variable1",],self.ProposalData[i].VoteID,self.ProposalData[i].VoteInitiator,self.ProposalData[i].TerseDateID,self.ProposalData[i].StartDateTime,self.ProposalData[i].EndDateTime,self.ProposalData[i].AlreadyVoted,self.ProposalData[i].VoteCast,self.ProposalData[i].Majority,self.ProposalData[i].Quorum,self.ProposalData[i].ProposalText)

		return output