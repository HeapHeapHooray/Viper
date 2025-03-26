# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	GroupLimit: "S32"

@dataclass
class GroupData:
	GroupID: "LLUUID"


class JoinGroupRequestExtended(Message):

	absolute_id = 4294902188 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.GroupData = GroupData(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","signed int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.GroupData = GroupData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: JoinGroupRequestExtended, 
Message Absolute ID: 4294902188
Blocks:
{self.AgentData}
{self.GroupData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","signed int32",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupLimit)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.GroupData.GroupID)

		return output