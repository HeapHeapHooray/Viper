# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"

@dataclass
class GroupData:
	GroupID: "LLUUID"
	GroupPowers: "U64"
	AcceptNotices: "BOOL"
	GroupInsigniaID: "LLUUID"
	Contribution: "S32"
	GroupName: "Variable 1"


class AgentGroupDataUpdate(Message):

	absolute_id = 4294902149 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.GroupData = [GroupData(*((None,)*6))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.GroupData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int64","unsigned byte","uuid","signed int32","variable1",],remaining_bytes)
			self.GroupData.append(GroupData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: AgentGroupDataUpdate, 
Message Absolute ID: 4294902149
Blocks:
{self.AgentData}
{self.GroupData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		blocks_count = len(self.GroupData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int64","unsigned byte","uuid","signed int32","variable1",],self.GroupData[i].GroupID,self.GroupData[i].GroupPowers,self.GroupData[i].AcceptNotices,self.GroupData[i].GroupInsigniaID,self.GroupData[i].Contribution,self.GroupData[i].GroupName)

		return output