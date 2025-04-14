# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class HeaderData:
	NewFolderID: "LLUUID"
HEADERDATA = HeaderData

@dataclass
class ObjectData:
	OldItemID: "LLUUID"
	OldFolderID: "LLUUID"
OBJECTDATA = ObjectData


class CreateNewOutfitAttachments(Message):

	absolute_id = 4294902158 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*2))
		self.HeaderData = HEADERDATA(*((None,)*1))
		self.ObjectData = [OBJECTDATA(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.HeaderData = HEADERDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
			self.ObjectData.append(OBJECTDATA(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: CreateNewOutfitAttachments, 
Message Absolute ID: 4294902158
Blocks:
{self.AgentData}
{self.HeaderData}
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.HeaderData.NewFolderID)

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.ObjectData[i].OldItemID,self.ObjectData[i].OldFolderID)

		return output