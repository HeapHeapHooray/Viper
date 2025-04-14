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
class QueryData:
	QueryID: "LLUUID"
	QueryText: "Variable 1"
	QueryFlags: "U32"
	Category: "S8"
	SimName: "Variable 1"
	QueryStart: "S32"
QUERYDATA = QueryData


class DirPlacesQuery(Message):

	absolute_id = 4294901793 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*2))

		self.QueryData = QUERYDATA(*((None,)*6))

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","unsigned int32","signed byte","variable1","signed int32",],remaining_bytes)
		self.QueryData = QUERYDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: DirPlacesQuery, Message Absolute ID: 4294901793, Blocks: {self.AgentData},{self.QueryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","unsigned int32","signed byte","variable1","signed int32",],self.QueryData.QueryID,self.QueryData.QueryText,self.QueryData.QueryFlags,self.QueryData.Category,self.QueryData.SimName,self.QueryData.QueryStart)

		return output