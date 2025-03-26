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


class ChildAgentPositionUpdate(Message):

	absolute_id = 27 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*12))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","unsigned int32","uuid","uuid","vector3","vector3","vector3","vector3","vector3","vector3","vector3","unsigned byte",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ChildAgentPositionUpdate, 
Message Absolute ID: 27
Blocks:
{self.AgentData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","unsigned int32","uuid","uuid","vector3","vector3","vector3","vector3","vector3","vector3","vector3","unsigned byte",],self.AgentData.RegionHandle,self.AgentData.ViewerCircuitCode,self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.AgentPos,self.AgentData.AgentVel,self.AgentData.Center,self.AgentData.Size,self.AgentData.AtAxis,self.AgentData.LeftAxis,self.AgentData.UpAxis,self.AgentData.ChangedGrid)

		return output