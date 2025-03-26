# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"

@dataclass
class QueryData:
	QueryID: "LLUUID"
	QueryFlags: "U32"
	EstateID: "U32"
	Godlike: "BOOL"


class DirPopularQueryBackend(Message):

	absolute_id = 4294901812 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.QueryData = QueryData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32","unsigned int32","unsigned byte",],remaining_bytes)
		self.QueryData = QueryData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: DirPopularQueryBackend, 
Message Absolute ID: 4294901812
Blocks:
{self.AgentData}
{self.QueryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32","unsigned int32","unsigned byte",],self.QueryData.QueryID,self.QueryData.QueryFlags,self.QueryData.EstateID,self.QueryData.Godlike)

		return output