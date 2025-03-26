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
	SequenceID: "S32"
	West: "F32"
	South: "F32"
	East: "F32"
	North: "F32"
	SnapSelection: "BOOL"


class ParcelPropertiesRequest(Message):

	absolute_id = 65291 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.ParcelData = ParcelData(*((None,)*6))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","float","float","float","float","unsigned byte",],remaining_bytes)
		self.ParcelData = ParcelData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelPropertiesRequest, 
Message Absolute ID: 65291
Blocks:
{self.AgentData}
{self.ParcelData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","float","float","float","float","unsigned byte",],self.ParcelData.SequenceID,self.ParcelData.West,self.ParcelData.South,self.ParcelData.East,self.ParcelData.North,self.ParcelData.SnapSelection)

		return output