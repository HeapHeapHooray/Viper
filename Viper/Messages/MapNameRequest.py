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

@dataclass
class NameData:
	Name: "Variable 1"


class MapNameRequest(Message):

	absolute_id = 4294902168 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*5))
		self.NameData = NameData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned int32","unsigned byte",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1",],remaining_bytes)
		self.NameData = NameData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: MapNameRequest, 
Message Absolute ID: 4294902168
Blocks:
{self.AgentData}
{self.NameData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned int32","unsigned byte",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.Flags,self.AgentData.EstateID,self.AgentData.Godlike)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1",],self.NameData.Name)

		return output