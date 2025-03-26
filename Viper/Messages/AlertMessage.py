# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AlertData:
	Message: "Variable 1"

@dataclass
class AlertInfo:
	Message: "Variable 1"
	ExtraParams: "Variable 1"

@dataclass
class AgentInfo:
	AgentID: "LLUUID"


class AlertMessage(Message):

	absolute_id = 4294901894 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AlertData = AlertData(*((None,)*1))
		self.AlertInfo = [AlertInfo(*((None,)*2))]
		self.AgentInfo = [AgentInfo(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1",],remaining_bytes)
		self.AlertData = AlertData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AlertInfo = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","variable1",],remaining_bytes)
			self.AlertInfo.append(AlertInfo(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AgentInfo = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.AgentInfo.append(AgentInfo(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: AlertMessage, 
Message Absolute ID: 4294901894
Blocks:
{self.AlertData}
{self.AlertInfo}
{self.AgentInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["variable1",],self.AlertData.Message)

		blocks_count = len(self.AlertInfo)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable1","variable1",],self.AlertInfo[i].Message,self.AlertInfo[i].ExtraParams)

		blocks_count = len(self.AgentInfo)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentInfo[i].AgentID)

		return output