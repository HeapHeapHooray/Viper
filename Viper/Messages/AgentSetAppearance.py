# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	SerialNum: "U32"
	Size: "LLVector3"
AGENTDATA = AgentData

@dataclass
class WearableData:
	CacheID: "LLUUID"
	TextureIndex: "U8"
WEARABLEDATA = WearableData

@dataclass
class ObjectData:
	TextureEntry: "Variable 2"
OBJECTDATA = ObjectData

@dataclass
class VisualParam:
	ParamValue: "U8"
VISUALPARAM = VisualParam


class AgentSetAppearance(Message):

	absolute_id = 4294901844 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*4))

		self.WearableData = [WEARABLEDATA(*((None,)*2))]

		self.ObjectData = OBJECTDATA(*((None,)*1))

		self.VisualParam = [VISUALPARAM(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32","vector3",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.WearableData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
			self.WearableData.append(WEARABLEDATA(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
		self.ObjectData = OBJECTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.VisualParam = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
			self.VisualParam.append(VISUALPARAM(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: AgentSetAppearance, Message Absolute ID: 4294901844, Blocks: {self.AgentData},{self.WearableData},{self.ObjectData},{self.VisualParam}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32","vector3",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.SerialNum,self.AgentData.Size)

		blocks_count = len(self.WearableData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte",],self.WearableData[i].CacheID,self.WearableData[i].TextureIndex)

		output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.ObjectData.TextureEntry)

		blocks_count = len(self.VisualParam)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.VisualParam[i].ParamValue)

		return output