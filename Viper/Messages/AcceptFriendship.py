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
class TransactionBlock:
	TransactionID: "LLUUID"
TRANSACTIONBLOCK = TransactionBlock

@dataclass
class FolderData:
	FolderID: "LLUUID"
FOLDERDATA = FolderData


class AcceptFriendship(Message):

	absolute_id = 4294902057 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*2))
		self.TransactionBlock = TRANSACTIONBLOCK(*((None,)*1))
		self.FolderData = [FOLDERDATA(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.TransactionBlock = TRANSACTIONBLOCK(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.FolderData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.FolderData.append(FOLDERDATA(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: AcceptFriendship, 
Message Absolute ID: 4294902057
Blocks:
{self.AgentData}
{self.TransactionBlock}
{self.FolderData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.TransactionBlock.TransactionID)

		blocks_count = len(self.FolderData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.FolderData[i].FolderID)

		return output