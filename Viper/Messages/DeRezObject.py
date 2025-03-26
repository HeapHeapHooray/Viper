# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class AgentBlock:
	GroupID: "LLUUID"
	Destination: "U8"
	DestinationID: "LLUUID"
	TransactionID: "LLUUID"
	PacketCount: "U8"
	PacketNumber: "U8"

@dataclass
class ObjectData:
	ObjectLocalID: "U32"


class DeRezObject(Message):

	absolute_id = 4294902051 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.AgentBlock = AgentBlock(*((None,)*6))
		self.ObjectData = [ObjectData(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte","uuid","uuid","unsigned byte","unsigned byte",],remaining_bytes)
		self.AgentBlock = AgentBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
			self.ObjectData.append(ObjectData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: DeRezObject, 
Message Absolute ID: 4294902051
Blocks:
{self.AgentData}
{self.AgentBlock}
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte","uuid","uuid","unsigned byte","unsigned byte",],self.AgentBlock.GroupID,self.AgentBlock.Destination,self.AgentBlock.DestinationID,self.AgentBlock.TransactionID,self.AgentBlock.PacketCount,self.AgentBlock.PacketNumber)

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.ObjectData[i].ObjectLocalID)

		return output