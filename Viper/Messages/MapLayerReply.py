# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	Flags: "U32"

@dataclass
class LayerData:
	Left: "U32"
	Right: "U32"
	Top: "U32"
	Bottom: "U32"
	ImageID: "LLUUID"


class MapLayerReply(Message):

	absolute_id = 4294902166 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.LayerData = [LayerData(*((None,)*5))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.LayerData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32","unsigned int32","uuid",],remaining_bytes)
			self.LayerData.append(LayerData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: MapLayerReply, 
Message Absolute ID: 4294902166
Blocks:
{self.AgentData}
{self.LayerData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32",],self.AgentData.AgentID,self.AgentData.Flags)

		blocks_count = len(self.LayerData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32","unsigned int32","uuid",],self.LayerData[i].Left,self.LayerData[i].Right,self.LayerData[i].Top,self.LayerData[i].Bottom,self.LayerData[i].ImageID)

		return output