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
	TextureID: "LLUUID"
	TextureIndex: "U8"
	HostName: "Variable 1"


class AgentCachedTextureResponse(Message):

	absolute_id = 4294902145 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.WearableData = [WearableData(*((None,)*3))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","signed int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.WearableData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte","variable1",],remaining_bytes)
			self.WearableData.append(WearableData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: AgentCachedTextureResponse, 
Message Absolute ID: 4294902145
Blocks:
{self.AgentData}
{self.WearableData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","signed int32",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.SerialNum)

		blocks_count = len(self.WearableData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte","variable1",],self.WearableData[i].TextureID,self.WearableData[i].TextureIndex,self.WearableData[i].HostName)

		return output