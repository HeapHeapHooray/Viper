# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Location:
	X: "U8"
	Y: "U8"
	Z: "U8"
LOCATION = Location

@dataclass
class Index:
	You: "S16"
	Prey: "S16"
INDEX = Index

@dataclass
class AgentData:
	AgentID: "LLUUID"
AGENTDATA = AgentData


class CoarseLocationUpdate(Message):

	absolute_id = 65286 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Location = [LOCATION(*((None,)*3))]
		self.Index = INDEX(*((None,)*2))
		self.AgentData = [AGENTDATA(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Location = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned byte","unsigned byte",],remaining_bytes)
			self.Location.append(LOCATION(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int16","signed int16",],remaining_bytes)
		self.Index = INDEX(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AgentData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.AgentData.append(AGENTDATA(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: CoarseLocationUpdate, 
Message Absolute ID: 65286
Blocks:
{self.Location}
{self.Index}
{self.AgentData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.Location)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned byte","unsigned byte",],self.Location[i].X,self.Location[i].Y,self.Location[i].Z)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int16","signed int16",],self.Index.You,self.Index.Prey)

		blocks_count = len(self.AgentData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData[i].AgentID)

		return output