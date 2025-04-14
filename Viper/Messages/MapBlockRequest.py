# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	Flags: "U32"
	EstateID: "U32"
	Godlike: "BOOL"
AGENTDATA = AgentData

@dataclass
class PositionData:
	MinX: "U16"
	MaxX: "U16"
	MinY: "U16"
	MaxY: "U16"
POSITIONDATA = PositionData


class MapBlockRequest(Message):

	absolute_id = 4294902167 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*5))
		self.PositionData = POSITIONDATA(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned int32","unsigned byte",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int16","unsigned int16","unsigned int16","unsigned int16",],remaining_bytes)
		self.PositionData = POSITIONDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: MapBlockRequest, 
Message Absolute ID: 4294902167
Blocks:
{self.AgentData}
{self.PositionData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned int32","unsigned byte",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.Flags,self.AgentData.EstateID,self.AgentData.Godlike)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int16","unsigned int16","unsigned int16","unsigned int16",],self.PositionData.MinX,self.PositionData.MaxX,self.PositionData.MinY,self.PositionData.MaxY)

		return output