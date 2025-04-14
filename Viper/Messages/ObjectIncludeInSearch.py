# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class ObjectData:
	ObjectLocalID: "U32"
	IncludeInSearch: "BOOL"
OBJECTDATA = ObjectData


class ObjectIncludeInSearch(Message):

	absolute_id = 4294902184 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*2))
		self.ObjectData = [OBJECTDATA(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned byte",],remaining_bytes)
			self.ObjectData.append(OBJECTDATA(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectIncludeInSearch, 
Message Absolute ID: 4294902184
Blocks:
{self.AgentData}
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned byte",],self.ObjectData[i].ObjectLocalID,self.ObjectData[i].IncludeInSearch)

		return output