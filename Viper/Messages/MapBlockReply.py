# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	Flags: "U32"

@dataclass
class Data:
	X: "U16"
	Y: "U16"
	Name: "Variable 1"
	Access: "U8"
	RegionFlags: "U32"
	WaterHeight: "U8"
	Agents: "U8"
	MapImageID: "LLUUID"


class MapBlockReply(Message):

	absolute_id = 4294902169 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.Data = [Data(*((None,)*8))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Data = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int16","unsigned int16","variable1","unsigned byte","unsigned int32","unsigned byte","unsigned byte","uuid",],remaining_bytes)
			self.Data.append(Data(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: MapBlockReply, 
Message Absolute ID: 4294902169
Blocks:
{self.AgentData}
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32",],self.AgentData.AgentID,self.AgentData.Flags)

		blocks_count = len(self.Data)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int16","unsigned int16","variable1","unsigned byte","unsigned int32","unsigned byte","unsigned byte","uuid",],self.Data[i].X,self.Data[i].Y,self.Data[i].Name,self.Data[i].Access,self.Data[i].RegionFlags,self.Data[i].WaterHeight,self.Data[i].Agents,self.Data[i].MapImageID)

		return output