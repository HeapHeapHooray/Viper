# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TransactionData:
	TransactionID: "LLUUID"
	TransactionTime: "U32"
	TransactionType: "S32"
	SourceID: "LLUUID"
	DestID: "LLUUID"
	Flags: "U8"
	Amount: "S32"
	SimulatorIP: "IPADDR"
	GridX: "U32"
	GridY: "U32"
	FailureType: "U8"


class LogFailedMoneyTransaction(Message):

	absolute_id = 4294901780 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TransactionData = TransactionData(*((None,)*11))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32","signed int32","uuid","uuid","unsigned byte","signed int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte",],remaining_bytes)
		self.TransactionData = TransactionData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: LogFailedMoneyTransaction, 
Message Absolute ID: 4294901780
Blocks:
{self.TransactionData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32","signed int32","uuid","uuid","unsigned byte","signed int32","unsigned int32","unsigned int32","unsigned int32","unsigned byte",],self.TransactionData.TransactionID,self.TransactionData.TransactionTime,self.TransactionData.TransactionType,self.TransactionData.SourceID,self.TransactionData.DestID,self.TransactionData.Flags,self.TransactionData.Amount,self.TransactionData.SimulatorIP,self.TransactionData.GridX,self.TransactionData.GridY,self.TransactionData.FailureType)

		return output