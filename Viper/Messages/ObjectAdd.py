# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	GroupID: "LLUUID"

@dataclass
class ObjectData:
	PCode: "U8"
	Material: "U8"
	AddFlags: "U32"
	PathCurve: "U8"
	ProfileCurve: "U8"
	PathBegin: "U16"
	PathEnd: "U16"
	PathScaleX: "U8"
	PathScaleY: "U8"
	PathShearX: "U8"
	PathShearY: "U8"
	PathTwist: "S8"
	PathTwistBegin: "S8"
	PathRadiusOffset: "S8"
	PathTaperX: "S8"
	PathTaperY: "S8"
	PathRevolutions: "U8"
	PathSkew: "S8"
	ProfileBegin: "U16"
	ProfileEnd: "U16"
	ProfileHollow: "U16"
	BypassRaycast: "U8"
	RayStart: "LLVector3"
	RayEnd: "LLVector3"
	RayTargetID: "LLUUID"
	RayEndIsIntersection: "U8"
	Scale: "LLVector3"
	Rotation: "LLQuaternion"
	State: "U8"


class ObjectAdd(Message):

	absolute_id = 65281 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.ObjectData = ObjectData(*((None,)*29))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned byte","unsigned int32","unsigned byte","unsigned byte","unsigned int16","unsigned int16","unsigned byte","unsigned byte","unsigned byte","unsigned byte","signed byte","signed byte","signed byte","signed byte","signed byte","unsigned byte","signed byte","unsigned int16","unsigned int16","unsigned int16","unsigned byte","vector3","vector3","uuid","unsigned byte","vector3","unit_quaternion","unsigned byte",],remaining_bytes)
		self.ObjectData = ObjectData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectAdd, 
Message Absolute ID: 65281
Blocks:
{self.AgentData}
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned byte","unsigned int32","unsigned byte","unsigned byte","unsigned int16","unsigned int16","unsigned byte","unsigned byte","unsigned byte","unsigned byte","signed byte","signed byte","signed byte","signed byte","signed byte","unsigned byte","signed byte","unsigned int16","unsigned int16","unsigned int16","unsigned byte","vector3","vector3","uuid","unsigned byte","vector3","unit_quaternion","unsigned byte",],self.ObjectData.PCode,self.ObjectData.Material,self.ObjectData.AddFlags,self.ObjectData.PathCurve,self.ObjectData.ProfileCurve,self.ObjectData.PathBegin,self.ObjectData.PathEnd,self.ObjectData.PathScaleX,self.ObjectData.PathScaleY,self.ObjectData.PathShearX,self.ObjectData.PathShearY,self.ObjectData.PathTwist,self.ObjectData.PathTwistBegin,self.ObjectData.PathRadiusOffset,self.ObjectData.PathTaperX,self.ObjectData.PathTaperY,self.ObjectData.PathRevolutions,self.ObjectData.PathSkew,self.ObjectData.ProfileBegin,self.ObjectData.ProfileEnd,self.ObjectData.ProfileHollow,self.ObjectData.BypassRaycast,self.ObjectData.RayStart,self.ObjectData.RayEnd,self.ObjectData.RayTargetID,self.ObjectData.RayEndIsIntersection,self.ObjectData.Scale,self.ObjectData.Rotation,self.ObjectData.State)

		return output