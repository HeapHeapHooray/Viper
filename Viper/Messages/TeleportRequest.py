# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class Info:
	RegionID: "LLUUID"
	Position: "LLVector3"
	LookAt: "LLVector3"


class TeleportRequest(Message):

	absolute_id = 4294901822 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.Info = Info(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","vector3","vector3",],remaining_bytes)
		self.Info = Info(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TeleportRequest, 
Message Absolute ID: 4294901822
Blocks:
{self.AgentData}
{self.Info}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","vector3","vector3",],self.Info.RegionID,self.Info.Position,self.Info.LookAt)

		return output