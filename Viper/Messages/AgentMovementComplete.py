# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class Data:
	Position: "LLVector3"
	LookAt: "LLVector3"
	RegionHandle: "U64"
	Timestamp: "U32"

@dataclass
class SimData:
	ChannelVersion: "Variable 2"


class AgentMovementComplete(Message):

	absolute_id = 4294902010 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.Data = Data(*((None,)*4))
		self.SimData = SimData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["vector3","vector3","unsigned int64","unsigned int32",],remaining_bytes)
		self.Data = Data(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
		self.SimData = SimData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AgentMovementComplete, 
Message Absolute ID: 4294902010
Blocks:
{self.AgentData}
{self.Data}
{self.SimData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["vector3","vector3","unsigned int64","unsigned int32",],self.Data.Position,self.Data.LookAt,self.Data.RegionHandle,self.Data.Timestamp)

		output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.SimData.ChannelVersion)

		return output