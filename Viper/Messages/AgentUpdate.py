# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	BodyRotation: "LLQuaternion"
	HeadRotation: "LLQuaternion"
	State: "U8"
	CameraCenter: "LLVector3"
	CameraAtAxis: "LLVector3"
	CameraLeftAxis: "LLVector3"
	CameraUpAxis: "LLVector3"
	Far: "F32"
	ControlFlags: "U32"
	Flags: "U8"


class AgentUpdate(Message):

	absolute_id = 4 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*12))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unit_quaternion","unit_quaternion","unsigned byte","vector3","vector3","vector3","vector3","float","unsigned int32","unsigned byte",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AgentUpdate, 
Message Absolute ID: 4
Blocks:
{self.AgentData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unit_quaternion","unit_quaternion","unsigned byte","vector3","vector3","vector3","vector3","float","unsigned int32","unsigned byte",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.BodyRotation,self.AgentData.HeadRotation,self.AgentData.State,self.AgentData.CameraCenter,self.AgentData.CameraAtAxis,self.AgentData.CameraLeftAxis,self.AgentData.CameraUpAxis,self.AgentData.Far,self.AgentData.ControlFlags,self.AgentData.Flags)

		return output