# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	GroupID: "LLUUID"

@dataclass
class MoneyData:
	RequestID: "LLUUID"
	IntervalDays: "S32"
	CurrentInterval: "S32"


class GroupAccountTransactionsRequest(Message):

	absolute_id = 4294902117 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.MoneyData = MoneyData(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","signed int32",],remaining_bytes)
		self.MoneyData = MoneyData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupAccountTransactionsRequest, 
Message Absolute ID: 4294902117
Blocks:
{self.AgentData}
{self.MoneyData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","signed int32",],self.MoneyData.RequestID,self.MoneyData.IntervalDays,self.MoneyData.CurrentInterval)

		return output