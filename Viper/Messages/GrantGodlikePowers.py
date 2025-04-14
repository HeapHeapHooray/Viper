# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class GrantData:
	GodLevel: "U8"
	Token: "LLUUID"
GRANTDATA = GrantData


class GrantGodlikePowers(Message):

	absolute_id = 4294902018 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*2))
		self.GrantData = GRANTDATA(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","uuid",],remaining_bytes)
		self.GrantData = GRANTDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: GrantGodlikePowers, 
Message Absolute ID: 4294902018
Blocks:
{self.AgentData}
{self.GrantData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","uuid",],self.GrantData.GodLevel,self.GrantData.Token)

		return output