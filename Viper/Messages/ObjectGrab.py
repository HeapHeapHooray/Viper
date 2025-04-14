# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class ObjectData:
	LocalID: "U32"
	GrabOffset: "LLVector3"
OBJECTDATA = ObjectData

@dataclass
class SurfaceInfo:
	UVCoord: "LLVector3"
	STCoord: "LLVector3"
	FaceIndex: "S32"
	Position: "LLVector3"
	Normal: "LLVector3"
	Binormal: "LLVector3"
SURFACEINFO = SurfaceInfo


class ObjectGrab(Message):

	absolute_id = 4294901877 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*2))

		self.ObjectData = OBJECTDATA(*((None,)*2))

		self.SurfaceInfo = [SURFACEINFO(*((None,)*6))]

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","vector3",],remaining_bytes)
		self.ObjectData = OBJECTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.SurfaceInfo = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["vector3","vector3","signed int32","vector3","vector3","vector3",],remaining_bytes)
			self.SurfaceInfo.append(SURFACEINFO(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectGrab, Message Absolute ID: 4294901877, Blocks: {self.AgentData},{self.ObjectData},{self.SurfaceInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","vector3",],self.ObjectData.LocalID,self.ObjectData.GrabOffset)

		blocks_count = len(self.SurfaceInfo)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["vector3","vector3","signed int32","vector3","vector3","vector3",],self.SurfaceInfo[i].UVCoord,self.SurfaceInfo[i].STCoord,self.SurfaceInfo[i].FaceIndex,self.SurfaceInfo[i].Position,self.SurfaceInfo[i].Normal,self.SurfaceInfo[i].Binormal)

		return output