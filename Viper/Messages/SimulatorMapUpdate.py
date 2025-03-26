# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class MapData:
	Flags: "U32"


class SimulatorMapUpdate(Message):

	absolute_id = 4294901765 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.MapData = MapData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
		self.MapData = MapData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SimulatorMapUpdate, 
Message Absolute ID: 4294901765
Blocks:
{self.MapData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.MapData.Flags)

		return output