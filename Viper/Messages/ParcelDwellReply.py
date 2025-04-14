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
class Data:
	LocalID: "S32"
	ParcelID: "LLUUID"
	Dwell: "F32"
DATA = Data


class ParcelDwellReply(Message):

	absolute_id = 4294901979 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*1))

		self.Data = DATA(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","uuid","float",],remaining_bytes)
		self.Data = DATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelDwellReply, Message Absolute ID: 4294901979, Blocks: {self.AgentData},{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","uuid","float",],self.Data.LocalID,self.Data.ParcelID,self.Data.Dwell)

		return output