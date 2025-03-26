# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class FailureInfo:
	ErrorMessage: "Variable 1"
	AgentID: "LLUUID"
	TransactionID: "LLUUID"


class FeatureDisabled(Message):

	absolute_id = 4294901779 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.FailureInfo = FailureInfo(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","uuid","uuid",],remaining_bytes)
		self.FailureInfo = FailureInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: FeatureDisabled, 
Message Absolute ID: 4294901779
Blocks:
{self.FailureInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","uuid","uuid",],self.FailureInfo.ErrorMessage,self.FailureInfo.AgentID,self.FailureInfo.TransactionID)

		return output