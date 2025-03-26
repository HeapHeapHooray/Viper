# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentBlock:
	Hunter: "LLUUID"
	Prey: "LLUUID"
	SpaceIP: "IPADDR"

@dataclass
class LocationBlock:
	GlobalX: "F64"
	GlobalY: "F64"


class FindAgent(Message):

	absolute_id = 4294902016 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentBlock = AgentBlock(*((None,)*3))
		self.LocationBlock = [LocationBlock(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32",],remaining_bytes)
		self.AgentBlock = AgentBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.LocationBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["double","double",],remaining_bytes)
			self.LocationBlock.append(LocationBlock(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: FindAgent, 
Message Absolute ID: 4294902016
Blocks:
{self.AgentBlock}
{self.LocationBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32",],self.AgentBlock.Hunter,self.AgentBlock.Prey,self.AgentBlock.SpaceIP)

		blocks_count = len(self.LocationBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["double","double",],self.LocationBlock[i].GlobalX,self.LocationBlock[i].GlobalY)

		return output