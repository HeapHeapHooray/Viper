# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	TexturesChanged: "BOOL"

@dataclass
class WearableData:
	CacheID: "LLUUID"
	TextureIndex: "U8"
	HostName: "Variable 1"

@dataclass
class TextureData:
	TextureID: "LLUUID"


class AvatarTextureUpdate(Message):

	absolute_id = 4294901764 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.WearableData = [WearableData(*((None,)*3))]
		self.TextureData = [TextureData(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.WearableData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte","variable1",],remaining_bytes)
			self.WearableData.append(WearableData(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.TextureData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.TextureData.append(TextureData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarTextureUpdate, 
Message Absolute ID: 4294901764
Blocks:
{self.AgentData}
{self.WearableData}
{self.TextureData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte",],self.AgentData.AgentID,self.AgentData.TexturesChanged)

		blocks_count = len(self.WearableData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte","variable1",],self.WearableData[i].CacheID,self.WearableData[i].TextureIndex,self.WearableData[i].HostName)

		blocks_count = len(self.TextureData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.TextureData[i].TextureID)

		return output