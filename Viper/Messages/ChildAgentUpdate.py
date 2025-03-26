# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	RegionHandle: "U64"
	ViewerCircuitCode: "U32"
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	AgentPos: "LLVector3"
	AgentVel: "LLVector3"
	Center: "LLVector3"
	Size: "LLVector3"
	AtAxis: "LLVector3"
	LeftAxis: "LLVector3"
	UpAxis: "LLVector3"
	ChangedGrid: "BOOL"
	Far: "F32"
	Aspect: "F32"
	Throttles: "Variable 1"
	LocomotionState: "U32"
	HeadRotation: "LLQuaternion"
	BodyRotation: "LLQuaternion"
	ControlFlags: "U32"
	EnergyLevel: "F32"
	GodLevel: "U8"
	AlwaysRun: "BOOL"
	PreyAgent: "LLUUID"
	AgentAccess: "U8"
	AgentTextures: "Variable 2"
	ActiveGroupID: "LLUUID"

@dataclass
class GroupData:
	GroupID: "LLUUID"
	GroupPowers: "U64"
	AcceptNotices: "BOOL"

@dataclass
class AnimationData:
	Animation: "LLUUID"
	ObjectID: "LLUUID"

@dataclass
class GranterBlock:
	GranterID: "LLUUID"

@dataclass
class NVPairData:
	NVPairs: "Variable 2"

@dataclass
class VisualParam:
	ParamValue: "U8"

@dataclass
class AgentAccess:
	AgentLegacyAccess: "U8"
	AgentMaxAccess: "U8"

@dataclass
class AgentInfo:
	Flags: "U32"

@dataclass
class AgentInventoryHost:
	InventoryHost: "Variable 1"


class ChildAgentUpdate(Message):

	absolute_id = 25 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*26))
		self.GroupData = [GroupData(*((None,)*3))]
		self.AnimationData = [AnimationData(*((None,)*2))]
		self.GranterBlock = [GranterBlock(*((None,)*1))]
		self.NVPairData = [NVPairData(*((None,)*1))]
		self.VisualParam = [VisualParam(*((None,)*1))]
		self.AgentAccess = [AgentAccess(*((None,)*2))]
		self.AgentInfo = [AgentInfo(*((None,)*1))]
		self.AgentInventoryHost = [AgentInventoryHost(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","unsigned int32","uuid","uuid","vector3","vector3","vector3","vector3","vector3","vector3","vector3","unsigned byte","float","float","variable1","unsigned int32","unit_quaternion","unit_quaternion","unsigned int32","float","unsigned byte","unsigned byte","uuid","unsigned byte","variable2","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.GroupData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int64","unsigned byte",],remaining_bytes)
			self.GroupData.append(GroupData(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AnimationData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
			self.AnimationData.append(AnimationData(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.GranterBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.GranterBlock.append(GranterBlock(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.NVPairData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
			self.NVPairData.append(NVPairData(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.VisualParam = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
			self.VisualParam.append(VisualParam(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AgentAccess = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned byte",],remaining_bytes)
			self.AgentAccess.append(AgentAccess(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AgentInfo = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
			self.AgentInfo.append(AgentInfo(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AgentInventoryHost = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1",],remaining_bytes)
			self.AgentInventoryHost.append(AgentInventoryHost(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ChildAgentUpdate, 
Message Absolute ID: 25
Blocks:
{self.AgentData}
{self.GroupData}
{self.AnimationData}
{self.GranterBlock}
{self.NVPairData}
{self.VisualParam}
{self.AgentAccess}
{self.AgentInfo}
{self.AgentInventoryHost}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","unsigned int32","uuid","uuid","vector3","vector3","vector3","vector3","vector3","vector3","vector3","unsigned byte","float","float","variable1","unsigned int32","unit_quaternion","unit_quaternion","unsigned int32","float","unsigned byte","unsigned byte","uuid","unsigned byte","variable2","uuid",],self.AgentData.RegionHandle,self.AgentData.ViewerCircuitCode,self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.AgentPos,self.AgentData.AgentVel,self.AgentData.Center,self.AgentData.Size,self.AgentData.AtAxis,self.AgentData.LeftAxis,self.AgentData.UpAxis,self.AgentData.ChangedGrid,self.AgentData.Far,self.AgentData.Aspect,self.AgentData.Throttles,self.AgentData.LocomotionState,self.AgentData.HeadRotation,self.AgentData.BodyRotation,self.AgentData.ControlFlags,self.AgentData.EnergyLevel,self.AgentData.GodLevel,self.AgentData.AlwaysRun,self.AgentData.PreyAgent,self.AgentData.AgentAccess,self.AgentData.AgentTextures,self.AgentData.ActiveGroupID)

		blocks_count = len(self.GroupData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int64","unsigned byte",],self.GroupData[i].GroupID,self.GroupData[i].GroupPowers,self.GroupData[i].AcceptNotices)

		blocks_count = len(self.AnimationData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AnimationData[i].Animation,self.AnimationData[i].ObjectID)

		blocks_count = len(self.GranterBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.GranterBlock[i].GranterID)

		blocks_count = len(self.NVPairData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.NVPairData[i].NVPairs)

		blocks_count = len(self.VisualParam)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.VisualParam[i].ParamValue)

		blocks_count = len(self.AgentAccess)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned byte",],self.AgentAccess[i].AgentLegacyAccess,self.AgentAccess[i].AgentMaxAccess)

		blocks_count = len(self.AgentInfo)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.AgentInfo[i].Flags)

		blocks_count = len(self.AgentInventoryHost)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable1",],self.AgentInventoryHost[i].InventoryHost)

		return output