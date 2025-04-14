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
	ReturnType: "U32"
PARCELDATA = ParcelData

@dataclass
class ReturnIDs:
	ReturnID: "LLUUID"
RETURNIDS = ReturnIDs


class ParcelSelectObjects(Message):

	absolute_id = 4294901962 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*2))

		self.ParcelData = PARCELDATA(*((None,)*2))

		self.ReturnIDs = [RETURNIDS(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","unsigned int32",],remaining_bytes)
		self.ParcelData = PARCELDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ReturnIDs = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.ReturnIDs.append(RETURNIDS(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelSelectObjects, Message Absolute ID: 4294901962, Blocks: {self.AgentData},{self.ParcelData},{self.ReturnIDs}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","unsigned int32",],self.ParcelData.LocalID,self.ParcelData.ReturnType)

		blocks_count = len(self.ReturnIDs)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.ReturnIDs[i].ReturnID)

		return output