# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class FileData:
	SimFilename: "Variable 1"
	ViewerFilename: "Variable 1"
FILEDATA = FileData


class InitiateDownload(Message):

	absolute_id = 4294902163 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*1))
		self.FileData = FILEDATA(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","variable1",],remaining_bytes)
		self.FileData = FILEDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: InitiateDownload, 
Message Absolute ID: 4294902163
Blocks:
{self.AgentData}
{self.FileData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","variable1",],self.FileData.SimFilename,self.FileData.ViewerFilename)

		return output