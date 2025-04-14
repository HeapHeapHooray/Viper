# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class QueryData:
	QueryID: "LLUUID"
QUERYDATA = QueryData

@dataclass
class QueryReplies:
	ParcelID: "LLUUID"
	Name: "Variable 1"
	ForSale: "BOOL"
	Auction: "BOOL"
	Dwell: "F32"
QUERYREPLIES = QueryReplies

@dataclass
class StatusData:
	Status: "U32"
STATUSDATA = StatusData


class DirPlacesReply(Message):

	absolute_id = 4294901795 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*1))
		self.QueryData = [QUERYDATA(*((None,)*1))]
		self.QueryReplies = [QUERYREPLIES(*((None,)*5))]
		self.StatusData = [STATUSDATA(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.QueryData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.QueryData.append(QUERYDATA(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.QueryReplies = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","unsigned byte","unsigned byte","float",],remaining_bytes)
			self.QueryReplies.append(QUERYREPLIES(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.StatusData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
			self.StatusData.append(STATUSDATA(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: DirPlacesReply, 
Message Absolute ID: 4294901795
Blocks:
{self.AgentData}
{self.QueryData}
{self.QueryReplies}
{self.StatusData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		blocks_count = len(self.QueryData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.QueryData[i].QueryID)

		blocks_count = len(self.QueryReplies)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","unsigned byte","unsigned byte","float",],self.QueryReplies[i].ParcelID,self.QueryReplies[i].Name,self.QueryReplies[i].ForSale,self.QueryReplies[i].Auction,self.QueryReplies[i].Dwell)

		blocks_count = len(self.StatusData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.StatusData[i].Status)

		return output