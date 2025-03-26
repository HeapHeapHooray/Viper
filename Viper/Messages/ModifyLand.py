# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class ModifyBlock:
	Action: "U8"
	BrushSize: "U8"
	Seconds: "F32"
	Height: "F32"

@dataclass
class ParcelData:
	LocalID: "S32"
	West: "F32"
	South: "F32"
	East: "F32"
	North: "F32"

@dataclass
class ModifyBlockExtended:
	BrushSize: "F32"


class ModifyLand(Message):

	absolute_id = 4294901884 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.ModifyBlock = ModifyBlock(*((None,)*4))
		self.ParcelData = [ParcelData(*((None,)*5))]
		self.ModifyBlockExtended = [ModifyBlockExtended(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned byte","float","float",],remaining_bytes)
		self.ModifyBlock = ModifyBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ParcelData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","float","float","float","float",],remaining_bytes)
			self.ParcelData.append(ParcelData(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ModifyBlockExtended = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["float",],remaining_bytes)
			self.ModifyBlockExtended.append(ModifyBlockExtended(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ModifyLand, 
Message Absolute ID: 4294901884
Blocks:
{self.AgentData}
{self.ModifyBlock}
{self.ParcelData}
{self.ModifyBlockExtended}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned byte","float","float",],self.ModifyBlock.Action,self.ModifyBlock.BrushSize,self.ModifyBlock.Seconds,self.ModifyBlock.Height)

		blocks_count = len(self.ParcelData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["signed int32","float","float","float","float",],self.ParcelData[i].LocalID,self.ParcelData[i].West,self.ParcelData[i].South,self.ParcelData[i].East,self.ParcelData[i].North)

		blocks_count = len(self.ModifyBlockExtended)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["float",],self.ModifyBlockExtended[i].BrushSize)

		return output