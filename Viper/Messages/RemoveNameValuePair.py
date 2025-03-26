# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TaskData:
	ID: "LLUUID"

@dataclass
class NameValueData:
	NVPair: "Variable 2"


class RemoveNameValuePair(Message):

	absolute_id = 4294902090 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TaskData = TaskData(*((None,)*1))
		self.NameValueData = [NameValueData(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.TaskData = TaskData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.NameValueData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
			self.NameValueData.append(NameValueData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: RemoveNameValuePair, 
Message Absolute ID: 4294902090
Blocks:
{self.TaskData}
{self.NameValueData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.TaskData.ID)

		blocks_count = len(self.NameValueData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.NameValueData[i].NVPair)

		return output