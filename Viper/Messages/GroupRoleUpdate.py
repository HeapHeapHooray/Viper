# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	GroupID: "LLUUID"

@dataclass
class RoleData:
	RoleID: "LLUUID"
	Name: "Variable 1"
	Description: "Variable 1"
	Title: "Variable 1"
	Powers: "U64"
	UpdateType: "U8"


class GroupRoleUpdate(Message):

	absolute_id = 4294902138 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.RoleData = [RoleData(*((None,)*6))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.RoleData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","variable1","variable1","unsigned int64","unsigned byte",],remaining_bytes)
			self.RoleData.append(RoleData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: GroupRoleUpdate, 
Message Absolute ID: 4294902138
Blocks:
{self.AgentData}
{self.RoleData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupID)

		blocks_count = len(self.RoleData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","variable1","variable1","unsigned int64","unsigned byte",],self.RoleData[i].RoleID,self.RoleData[i].Name,self.RoleData[i].Description,self.RoleData[i].Title,self.RoleData[i].Powers,self.RoleData[i].UpdateType)

		return output