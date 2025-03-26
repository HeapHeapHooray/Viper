# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	GroupID: "LLUUID"

@dataclass
class MoneyData:
	RequestID: "LLUUID"
	IntervalDays: "S32"
	CurrentInterval: "S32"
	StartDate: "Variable 1"
	Balance: "S32"
	TotalCredits: "S32"
	TotalDebits: "S32"
	ObjectTaxCurrent: "S32"
	LightTaxCurrent: "S32"
	LandTaxCurrent: "S32"
	GroupTaxCurrent: "S32"
	ParcelDirFeeCurrent: "S32"
	ObjectTaxEstimate: "S32"
	LightTaxEstimate: "S32"
	LandTaxEstimate: "S32"
	GroupTaxEstimate: "S32"
	ParcelDirFeeEstimate: "S32"
	NonExemptMembers: "S32"
	LastTaxDate: "Variable 1"
	TaxDate: "Variable 1"


class GroupAccountSummaryReply(Message):

	absolute_id = 4294902114 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.MoneyData = MoneyData(*((None,)*20))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","signed int32","variable1","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","variable1","variable1",],remaining_bytes)
		self.MoneyData = MoneyData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupAccountSummaryReply, 
Message Absolute ID: 4294902114
Blocks:
{self.AgentData}
{self.MoneyData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","signed int32","variable1","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","variable1","variable1",],self.MoneyData.RequestID,self.MoneyData.IntervalDays,self.MoneyData.CurrentInterval,self.MoneyData.StartDate,self.MoneyData.Balance,self.MoneyData.TotalCredits,self.MoneyData.TotalDebits,self.MoneyData.ObjectTaxCurrent,self.MoneyData.LightTaxCurrent,self.MoneyData.LandTaxCurrent,self.MoneyData.GroupTaxCurrent,self.MoneyData.ParcelDirFeeCurrent,self.MoneyData.ObjectTaxEstimate,self.MoneyData.LightTaxEstimate,self.MoneyData.LandTaxEstimate,self.MoneyData.GroupTaxEstimate,self.MoneyData.ParcelDirFeeEstimate,self.MoneyData.NonExemptMembers,self.MoneyData.LastTaxDate,self.MoneyData.TaxDate)

		return output