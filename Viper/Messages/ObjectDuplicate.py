# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	GroupID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class SharedData:
	Offset: "LLVector3"
	DuplicateFlags: "U32"
SHAREDDATA = SharedData

@dataclass
class ObjectData:
	ObjectLocalID: "U32"
OBJECTDATA = ObjectData


class ObjectDuplicate(Message):

	absolute_id = 4294901850 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*3))

		self.SharedData = SHAREDDATA(*((None,)*2))

		self.ObjectData = [OBJECTDATA(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["vector3","unsigned int32",],remaining_bytes)
		self.SharedData = SHAREDDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
			self.ObjectData.append(OBJECTDATA(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectDuplicate, Message Absolute ID: 4294901850, Blocks: {self.AgentData},{self.SharedData},{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["vector3","unsigned int32",],self.SharedData.Offset,self.SharedData.DuplicateFlags)

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.ObjectData[i].ObjectLocalID)

		return output