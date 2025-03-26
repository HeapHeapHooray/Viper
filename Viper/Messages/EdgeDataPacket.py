# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class EdgeData:
	LayerType: "U8"
	Direction: "U8"
	LayerData: "Variable 2"


class EdgeDataPacket(Message):

	absolute_id = 24 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.EdgeData = EdgeData(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned byte","variable2",],remaining_bytes)
		self.EdgeData = EdgeData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: EdgeDataPacket, 
Message Absolute ID: 24
Blocks:
{self.EdgeData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned byte","variable2",],self.EdgeData.LayerType,self.EdgeData.Direction,self.EdgeData.LayerData)

		return output