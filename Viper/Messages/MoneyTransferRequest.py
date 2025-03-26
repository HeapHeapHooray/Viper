# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class MoneyData:
	SourceID: "LLUUID"
	DestID: "LLUUID"
	Flags: "U8"
	Amount: "S32"
	AggregatePermNextOwner: "U8"
	AggregatePermInventory: "U8"
	TransactionType: "S32"
	Description: "Variable 1"


class MoneyTransferRequest(Message):

	absolute_id = 4294902071 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.MoneyData = MoneyData(*((None,)*8))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte","signed int32","unsigned byte","unsigned byte","signed int32","variable1",],remaining_bytes)
		self.MoneyData = MoneyData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: MoneyTransferRequest, 
Message Absolute ID: 4294902071
Blocks:
{self.AgentData}
{self.MoneyData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte","signed int32","unsigned byte","unsigned byte","signed int32","variable1",],self.MoneyData.SourceID,self.MoneyData.DestID,self.MoneyData.Flags,self.MoneyData.Amount,self.MoneyData.AggregatePermNextOwner,self.MoneyData.AggregatePermInventory,self.MoneyData.TransactionType,self.MoneyData.Description)

		return output