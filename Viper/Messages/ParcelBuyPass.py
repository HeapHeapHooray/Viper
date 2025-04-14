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
class ParcelData:
	LocalID: "S32"
PARCELDATA = ParcelData


class ParcelBuyPass(Message):

	absolute_id = 4294901966 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*2))

		self.ParcelData = PARCELDATA(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32",],remaining_bytes)
		self.ParcelData = PARCELDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelBuyPass, Message Absolute ID: 4294901966, Blocks: {self.AgentData},{self.ParcelData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32",],self.ParcelData.LocalID)

		return output