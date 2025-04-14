# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class AlertData:
	Modal: "BOOL"
	Message: "Variable 1"
ALERTDATA = AlertData


class AgentAlertMessage(Message):

	absolute_id = 4294901895 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*1))

		self.AlertData = ALERTDATA(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","variable1",],remaining_bytes)
		self.AlertData = ALERTDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AgentAlertMessage, Message Absolute ID: 4294901895, Blocks: {self.AgentData},{self.AlertData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","variable1",],self.AlertData.Modal,self.AlertData.Message)

		return output