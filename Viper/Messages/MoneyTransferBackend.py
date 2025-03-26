# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class MoneyData:
	TransactionID: "LLUUID"
	TransactionTime: "U32"
	SourceID: "LLUUID"
	DestID: "LLUUID"
	Flags: "U8"
	Amount: "S32"
	AggregatePermNextOwner: "U8"
	AggregatePermInventory: "U8"
	TransactionType: "S32"
	RegionID: "LLUUID"
	GridX: "U32"
	GridY: "U32"
	Description: "Variable 1"


class MoneyTransferBackend(Message):

	absolute_id = 4294902072 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.MoneyData = MoneyData(*((None,)*13))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32","uuid","uuid","unsigned byte","signed int32","unsigned byte","unsigned byte","signed int32","uuid","unsigned int32","unsigned int32","variable1",],remaining_bytes)
		self.MoneyData = MoneyData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: MoneyTransferBackend, 
Message Absolute ID: 4294902072
Blocks:
{self.MoneyData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32","uuid","uuid","unsigned byte","signed int32","unsigned byte","unsigned byte","signed int32","uuid","unsigned int32","unsigned int32","variable1",],self.MoneyData.TransactionID,self.MoneyData.TransactionTime,self.MoneyData.SourceID,self.MoneyData.DestID,self.MoneyData.Flags,self.MoneyData.Amount,self.MoneyData.AggregatePermNextOwner,self.MoneyData.AggregatePermInventory,self.MoneyData.TransactionType,self.MoneyData.RegionID,self.MoneyData.GridX,self.MoneyData.GridY,self.MoneyData.Description)

		return output