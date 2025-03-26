# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	QueryID: "LLUUID"
	GodLevel: "U8"

@dataclass
class Data:
	Name: "Variable 1"


class AvatarPickerRequestBackend(Message):

	absolute_id = 4294901787 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*4))
		self.Data = Data(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","unsigned byte",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1",],remaining_bytes)
		self.Data = Data(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarPickerRequestBackend, 
Message Absolute ID: 4294901787
Blocks:
{self.AgentData}
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","unsigned byte",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.QueryID,self.AgentData.GodLevel)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1",],self.Data.Name)

		return output