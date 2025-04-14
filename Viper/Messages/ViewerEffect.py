# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class Effect:
	ID: "LLUUID"
	AgentID: "LLUUID"
	Type: "U8"
	Duration: "F32"
	Color: "Fixed 4"
	TypeData: "Variable 1"
EFFECT = Effect


class ViewerEffect(Message):

	absolute_id = 65297 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*2))
		self.Effect = [EFFECT(*((None,)*6))]

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Effect = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte","float","unsigned int32","variable1",],remaining_bytes)
			self.Effect.append(EFFECT(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ViewerEffect, 
Message Absolute ID: 65297
Blocks:
{self.AgentData}
{self.Effect}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		blocks_count = len(self.Effect)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte","float","unsigned int32","variable1",],self.Effect[i].ID,self.Effect[i].AgentID,self.Effect[i].Type,self.Effect[i].Duration,self.Effect[i].Color,self.Effect[i].TypeData)

		return output