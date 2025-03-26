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

@dataclass
class QueryReplies:
	GroupID: "LLUUID"
	GroupName: "Variable 1"
	Members: "S32"
	SearchOrder: "F32"


class DirGroupsReply(Message):

	absolute_id = 4294901798 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.QueryData = QueryData(*((None,)*1))
		self.QueryReplies = [QueryReplies(*((None,)*4))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.QueryData = QueryData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.QueryReplies = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","signed int32","float",],remaining_bytes)
			self.QueryReplies.append(QueryReplies(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: DirGroupsReply, 
Message Absolute ID: 4294901798
Blocks:
{self.AgentData}
{self.QueryData}
{self.QueryReplies}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.QueryData.QueryID)

		blocks_count = len(self.QueryReplies)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","signed int32","float",],self.QueryReplies[i].GroupID,self.QueryReplies[i].GroupName,self.QueryReplies[i].Members,self.QueryReplies[i].SearchOrder)

		return output