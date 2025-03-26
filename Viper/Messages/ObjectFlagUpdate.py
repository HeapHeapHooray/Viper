# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	ObjectLocalID: "U32"
	UsePhysics: "BOOL"
	IsTemporary: "BOOL"
	IsPhantom: "BOOL"
	CastsShadows: "BOOL"

@dataclass
class ExtraPhysics:
	PhysicsShapeType: "U8"
	Density: "F32"
	Friction: "F32"
	Restitution: "F32"
	GravityMultiplier: "F32"


class ObjectFlagUpdate(Message):

	absolute_id = 4294901854 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*7))
		self.ExtraPhysics = [ExtraPhysics(*((None,)*5))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned byte","unsigned byte","unsigned byte","unsigned byte",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ExtraPhysics = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","float","float","float","float",],remaining_bytes)
			self.ExtraPhysics.append(ExtraPhysics(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectFlagUpdate, 
Message Absolute ID: 4294901854
Blocks:
{self.AgentData}
{self.ExtraPhysics}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned byte","unsigned byte","unsigned byte","unsigned byte",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.ObjectLocalID,self.AgentData.UsePhysics,self.AgentData.IsTemporary,self.AgentData.IsPhantom,self.AgentData.CastsShadows)

		blocks_count = len(self.ExtraPhysics)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","float","float","float","float",],self.ExtraPhysics[i].PhysicsShapeType,self.ExtraPhysics[i].Density,self.ExtraPhysics[i].Friction,self.ExtraPhysics[i].Restitution,self.ExtraPhysics[i].GravityMultiplier)

		return output