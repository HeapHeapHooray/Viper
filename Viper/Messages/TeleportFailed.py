# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Info:
	AgentID: "LLUUID"
	Reason: "Variable 1"

@dataclass
class AlertInfo:
	Message: "Variable 1"
	ExtraParams: "Variable 1"


class TeleportFailed(Message):

	absolute_id = 4294901834 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Info = Info(*((None,)*2))
		self.AlertInfo = [AlertInfo(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1",],remaining_bytes)
		self.Info = Info(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AlertInfo = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","variable1",],remaining_bytes)
			self.AlertInfo.append(AlertInfo(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: TeleportFailed, 
Message Absolute ID: 4294901834
Blocks:
{self.Info}
{self.AlertInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1",],self.Info.AgentID,self.Info.Reason)

		blocks_count = len(self.AlertInfo)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable1","variable1",],self.AlertInfo[i].Message,self.AlertInfo[i].ExtraParams)

		return output