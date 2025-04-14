# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	GroupID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class MoneyData:
	RequestID: "LLUUID"
	IntervalDays: "S32"
	CurrentInterval: "S32"
	StartDate: "Variable 1"
MONEYDATA = MoneyData

@dataclass
class HistoryData:
	Description: "Variable 1"
	Amount: "S32"
HISTORYDATA = HistoryData


class GroupAccountDetailsReply(Message):

	absolute_id = 4294902116 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*2))

		self.MoneyData = MONEYDATA(*((None,)*4))

		self.HistoryData = [HISTORYDATA(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","signed int32","variable1",],remaining_bytes)
		self.MoneyData = MONEYDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.HistoryData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","signed int32",],remaining_bytes)
			self.HistoryData.append(HISTORYDATA(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupAccountDetailsReply, Message Absolute ID: 4294902116, Blocks: {self.AgentData},{self.MoneyData},{self.HistoryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","signed int32","variable1",],self.MoneyData.RequestID,self.MoneyData.IntervalDays,self.MoneyData.CurrentInterval,self.MoneyData.StartDate)

		blocks_count = len(self.HistoryData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable1","signed int32",],self.HistoryData[i].Description,self.HistoryData[i].Amount)

		return output