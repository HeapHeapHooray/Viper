# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class ProposalData:
	GroupID: "LLUUID"
	Quorum: "S32"
	Majority: "F32"
	Duration: "S32"
	ProposalText: "Variable 1"


class StartGroupProposal(Message):

	absolute_id = 4294902123 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.ProposalData = ProposalData(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","float","signed int32","variable1",],remaining_bytes)
		self.ProposalData = ProposalData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: StartGroupProposal, 
Message Absolute ID: 4294902123
Blocks:
{self.AgentData}
{self.ProposalData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","float","signed int32","variable1",],self.ProposalData.GroupID,self.ProposalData.Quorum,self.ProposalData.Majority,self.ProposalData.Duration,self.ProposalData.ProposalText)

		return output