# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class RegionData:
	SimIP: "IPADDR"
	SimPort: "IPPORT"
	RegionHandle: "U64"
	SeedCapability: "Variable 2"

@dataclass
class Info:
	Position: "LLVector3"
	LookAt: "LLVector3"


class CrossedRegion(Message):

	absolute_id = 65287 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.RegionData = RegionData(*((None,)*4))
		self.Info = Info(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int16","unsigned int64","variable2",],remaining_bytes)
		self.RegionData = RegionData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["vector3","vector3",],remaining_bytes)
		self.Info = Info(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: CrossedRegion, 
Message Absolute ID: 65287
Blocks:
{self.AgentData}
{self.RegionData}
{self.Info}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int16","unsigned int64","variable2",],self.RegionData.SimIP,self.RegionData.SimPort,self.RegionData.RegionHandle,self.RegionData.SeedCapability)

		output = output + BytesUtils.pack_bytes_little_endian(["vector3","vector3",],self.Info.Position,self.Info.LookAt)

		return output