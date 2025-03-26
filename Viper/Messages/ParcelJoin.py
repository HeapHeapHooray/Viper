# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class ParcelData:
	West: "F32"
	South: "F32"
	East: "F32"
	North: "F32"


class ParcelJoin(Message):

	absolute_id = 4294901970 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.ParcelData = ParcelData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["float","float","float","float",],remaining_bytes)
		self.ParcelData = ParcelData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelJoin, 
Message Absolute ID: 4294901970
Blocks:
{self.AgentData}
{self.ParcelData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["float","float","float","float",],self.ParcelData.West,self.ParcelData.South,self.ParcelData.East,self.ParcelData.North)

		return output