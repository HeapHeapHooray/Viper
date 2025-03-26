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
class HistoryItemData:
	VoteID: "LLUUID"
	TerseDateID: "Variable 1"
	StartDateTime: "Variable 1"
	EndDateTime: "Variable 1"
	VoteInitiator: "LLUUID"
	VoteType: "Variable 1"
	VoteResult: "Variable 1"
	Majority: "F32"
	Quorum: "S32"
	ProposalText: "Variable 2"

@dataclass
class VoteItem:
	CandidateID: "LLUUID"
	VoteCast: "Variable 1"
	NumVotes: "S32"


class GroupVoteHistoryItemReply(Message):

	absolute_id = 4294902122 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.TransactionData = TransactionData(*((None,)*2))
		self.HistoryItemData = HistoryItemData(*((None,)*10))
		self.VoteItem = [VoteItem(*((None,)*3))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32",],remaining_bytes)
		self.TransactionData = TransactionData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","variable1","variable1","uuid","variable1","variable1","float","signed int32","variable2",],remaining_bytes)
		self.HistoryItemData = HistoryItemData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.VoteItem = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","signed int32",],remaining_bytes)
			self.VoteItem.append(VoteItem(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupVoteHistoryItemReply, 
Message Absolute ID: 4294902122
Blocks:
{self.AgentData}
{self.TransactionData}
{self.HistoryItemData}
{self.VoteItem}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32",],self.TransactionData.TransactionID,self.TransactionData.TotalNumItems)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","variable1","variable1","uuid","variable1","variable1","float","signed int32","variable2",],self.HistoryItemData.VoteID,self.HistoryItemData.TerseDateID,self.HistoryItemData.StartDateTime,self.HistoryItemData.EndDateTime,self.HistoryItemData.VoteInitiator,self.HistoryItemData.VoteType,self.HistoryItemData.VoteResult,self.HistoryItemData.Majority,self.HistoryItemData.Quorum,self.HistoryItemData.ProposalText)

		blocks_count = len(self.VoteItem)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","signed int32",],self.VoteItem[i].CandidateID,self.VoteItem[i].VoteCast,self.VoteItem[i].NumVotes)

		return output