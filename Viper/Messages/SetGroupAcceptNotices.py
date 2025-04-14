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
class Data:
	GroupID: "LLUUID"
	AcceptNotices: "BOOL"
DATA = Data

@dataclass
class NewData:
	ListInProfile: "BOOL"
NEWDATA = NewData


class SetGroupAcceptNotices(Message):

	absolute_id = 4294902130 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*2))

		self.Data = DATA(*((None,)*2))

		self.NewData = NEWDATA(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
		self.Data = DATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
		self.NewData = NEWDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SetGroupAcceptNotices, Message Absolute ID: 4294902130, Blocks: {self.AgentData},{self.Data},{self.NewData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte",],self.Data.GroupID,self.Data.AcceptNotices)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.NewData.ListInProfile)

		return output