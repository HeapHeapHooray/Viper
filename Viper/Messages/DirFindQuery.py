# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class QueryData:
	QueryID: "LLUUID"
	QueryText: "Variable 1"
	QueryFlags: "U32"
	QueryStart: "S32"


class DirFindQuery(Message):

	absolute_id = 4294901791 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.QueryData = QueryData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","unsigned int32","signed int32",],remaining_bytes)
		self.QueryData = QueryData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: DirFindQuery, 
Message Absolute ID: 4294901791
Blocks:
{self.AgentData}
{self.QueryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","unsigned int32","signed int32",],self.QueryData.QueryID,self.QueryData.QueryText,self.QueryData.QueryFlags,self.QueryData.QueryStart)

		return output