# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	GroupID: "LLUUID"
	RayStart: "LLVector3"
	RayEnd: "LLVector3"
	BypassRaycast: "BOOL"
	RayEndIsIntersection: "BOOL"
	CopyCenters: "BOOL"
	CopyRotates: "BOOL"
	RayTargetID: "LLUUID"
	DuplicateFlags: "U32"

@dataclass
class ObjectData:
	ObjectLocalID: "U32"


class ObjectDuplicateOnRay(Message):

	absolute_id = 4294901851 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*11))
		self.ObjectData = [ObjectData(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","vector3","vector3","unsigned byte","unsigned byte","unsigned byte","unsigned byte","uuid","unsigned int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
			self.ObjectData.append(ObjectData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectDuplicateOnRay, 
Message Absolute ID: 4294901851
Blocks:
{self.AgentData}
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","vector3","vector3","unsigned byte","unsigned byte","unsigned byte","unsigned byte","uuid","unsigned int32",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupID,self.AgentData.RayStart,self.AgentData.RayEnd,self.AgentData.BypassRaycast,self.AgentData.RayEndIsIntersection,self.AgentData.CopyCenters,self.AgentData.CopyRotates,self.AgentData.RayTargetID,self.AgentData.DuplicateFlags)

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.ObjectData[i].ObjectLocalID)

		return output