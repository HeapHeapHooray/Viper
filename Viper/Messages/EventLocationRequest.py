# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class QueryData:
	QueryID: "LLUUID"

@dataclass
class EventData:
	EventID: "U32"


class EventLocationRequest(Message):

	absolute_id = 4294902067 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.QueryData = QueryData(*((None,)*1))
		self.EventData = EventData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.QueryData = QueryData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
		self.EventData = EventData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: EventLocationRequest, 
Message Absolute ID: 4294902067
Blocks:
{self.QueryData}
{self.EventData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.QueryData.QueryID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.EventData.EventID)

		return output