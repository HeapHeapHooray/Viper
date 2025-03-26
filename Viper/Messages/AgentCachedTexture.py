# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	SerialNum: "S32"

@dataclass
class WearableData:
	ID: "LLUUID"
	TextureIndex: "U8"


class AgentCachedTexture(Message):

	absolute_id = 4294902144 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.WearableData = [WearableData(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","signed int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.WearableData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
			self.WearableData.append(WearableData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: AgentCachedTexture, 
Message Absolute ID: 4294902144
Blocks:
{self.AgentData}
{self.WearableData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","signed int32",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.SerialNum)

		blocks_count = len(self.WearableData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte",],self.WearableData[i].ID,self.WearableData[i].TextureIndex)

		return output