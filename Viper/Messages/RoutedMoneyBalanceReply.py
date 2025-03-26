# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TargetBlock:
	TargetIP: "IPADDR"
	TargetPort: "IPPORT"

@dataclass
class MoneyData:
	AgentID: "LLUUID"
	TransactionID: "LLUUID"
	TransactionSuccess: "BOOL"
	MoneyBalance: "S32"
	SquareMetersCredit: "S32"
	SquareMetersCommitted: "S32"
	Description: "Variable 1"

@dataclass
class TransactionInfo:
	TransactionType: "S32"
	SourceID: "LLUUID"
	IsSourceGroup: "BOOL"
	DestID: "LLUUID"
	IsDestGroup: "BOOL"
	Amount: "S32"
	ItemDescription: "Variable 1"


class RoutedMoneyBalanceReply(Message):

	absolute_id = 4294902075 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TargetBlock = TargetBlock(*((None,)*2))
		self.MoneyData = MoneyData(*((None,)*7))
		self.TransactionInfo = TransactionInfo(*((None,)*7))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int16",],remaining_bytes)
		self.TargetBlock = TargetBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte","signed int32","signed int32","signed int32","variable1",],remaining_bytes)
		self.MoneyData = MoneyData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","uuid","unsigned byte","uuid","unsigned byte","signed int32","variable1",],remaining_bytes)
		self.TransactionInfo = TransactionInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RoutedMoneyBalanceReply, 
Message Absolute ID: 4294902075
Blocks:
{self.TargetBlock}
{self.MoneyData}
{self.TransactionInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int16",],self.TargetBlock.TargetIP,self.TargetBlock.TargetPort)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte","signed int32","signed int32","signed int32","variable1",],self.MoneyData.AgentID,self.MoneyData.TransactionID,self.MoneyData.TransactionSuccess,self.MoneyData.MoneyBalance,self.MoneyData.SquareMetersCredit,self.MoneyData.SquareMetersCommitted,self.MoneyData.Description)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","uuid","unsigned byte","uuid","unsigned byte","signed int32","variable1",],self.TransactionInfo.TransactionType,self.TransactionInfo.SourceID,self.TransactionInfo.IsSourceGroup,self.TransactionInfo.DestID,self.TransactionInfo.IsDestGroup,self.TransactionInfo.Amount,self.TransactionInfo.ItemDescription)

		return output