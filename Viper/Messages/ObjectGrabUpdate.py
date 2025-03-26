# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class ObjectData:
	ObjectID: "LLUUID"
	GrabOffsetInitial: "LLVector3"
	GrabPosition: "LLVector3"
	TimeSinceLast: "U32"

@dataclass
class SurfaceInfo:
	UVCoord: "LLVector3"
	STCoord: "LLVector3"
	FaceIndex: "S32"
	Position: "LLVector3"
	Normal: "LLVector3"
	Binormal: "LLVector3"


class ObjectGrabUpdate(Message):

	absolute_id = 4294901878 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.ObjectData = ObjectData(*((None,)*4))
		self.SurfaceInfo = [SurfaceInfo(*((None,)*6))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","vector3","vector3","unsigned int32",],remaining_bytes)
		self.ObjectData = ObjectData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.SurfaceInfo = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["vector3","vector3","signed int32","vector3","vector3","vector3",],remaining_bytes)
			self.SurfaceInfo.append(SurfaceInfo(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectGrabUpdate, 
Message Absolute ID: 4294901878
Blocks:
{self.AgentData}
{self.ObjectData}
{self.SurfaceInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","vector3","vector3","unsigned int32",],self.ObjectData.ObjectID,self.ObjectData.GrabOffsetInitial,self.ObjectData.GrabPosition,self.ObjectData.TimeSinceLast)

		blocks_count = len(self.SurfaceInfo)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["vector3","vector3","signed int32","vector3","vector3","vector3",],self.SurfaceInfo[i].UVCoord,self.SurfaceInfo[i].STCoord,self.SurfaceInfo[i].FaceIndex,self.SurfaceInfo[i].Position,self.SurfaceInfo[i].Normal,self.SurfaceInfo[i].Binormal)

		return output