# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class MapData:
	RegionHandle: "U64"
	Type: "S32"
	MapImage: "LLUUID"


class SimulatorSetMap(Message):

	absolute_id = 4294901766 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.MapData = MapData(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","signed int32","uuid",],remaining_bytes)
		self.MapData = MapData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SimulatorSetMap, 
Message Absolute ID: 4294901766
Blocks:
{self.MapData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","signed int32","uuid",],self.MapData.RegionHandle,self.MapData.Type,self.MapData.MapImage)

		return output