# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class StartLocationData:
	SimName: "Variable 1"
	LocationID: "U32"
	LocationPos: "LLVector3"
	LocationLookAt: "LLVector3"


class SetStartLocationRequest(Message):

	absolute_id = 4294902084 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.StartLocationData = StartLocationData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","unsigned int32","vector3","vector3",],remaining_bytes)
		self.StartLocationData = StartLocationData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SetStartLocationRequest, 
Message Absolute ID: 4294902084
Blocks:
{self.AgentData}
{self.StartLocationData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","unsigned int32","vector3","vector3",],self.StartLocationData.SimName,self.StartLocationData.LocationID,self.StartLocationData.LocationPos,self.StartLocationData.LocationLookAt)

		return output