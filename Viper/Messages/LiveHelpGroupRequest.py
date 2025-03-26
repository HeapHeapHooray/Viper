# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class RequestData:
	RequestID: "LLUUID"
	AgentID: "LLUUID"


class LiveHelpGroupRequest(Message):

	absolute_id = 4294902139 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.RequestData = RequestData(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.RequestData = RequestData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: LiveHelpGroupRequest, 
Message Absolute ID: 4294902139
Blocks:
{self.RequestData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.RequestData.RequestID,self.RequestData.AgentID)

		return output