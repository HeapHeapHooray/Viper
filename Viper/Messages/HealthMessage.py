# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class HealthData:
	Health: "F32"


class HealthMessage(Message):

	absolute_id = 4294901898 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.HealthData = HealthData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["float",],remaining_bytes)
		self.HealthData = HealthData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: HealthMessage, 
Message Absolute ID: 4294901898
Blocks:
{self.HealthData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["float",],self.HealthData.Health)

		return output