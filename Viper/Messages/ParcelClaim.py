# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class Data:
	GroupID: "LLUUID"
	IsGroupOwned: "BOOL"
	Final: "BOOL"

@dataclass
class ParcelData:
	West: "F32"
	South: "F32"
	East: "F32"
	North: "F32"


class ParcelClaim(Message):

	absolute_id = 4294901969 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.Data = Data(*((None,)*3))
		self.ParcelData = [ParcelData(*((None,)*4))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte","unsigned byte",],remaining_bytes)
		self.Data = Data(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ParcelData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["float","float","float","float",],remaining_bytes)
			self.ParcelData.append(ParcelData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelClaim, 
Message Absolute ID: 4294901969
Blocks:
{self.AgentData}
{self.Data}
{self.ParcelData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte","unsigned byte",],self.Data.GroupID,self.Data.IsGroupOwned,self.Data.Final)

		blocks_count = len(self.ParcelData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["float","float","float","float",],self.ParcelData[i].West,self.ParcelData[i].South,self.ParcelData[i].East,self.ParcelData[i].North)

		return output