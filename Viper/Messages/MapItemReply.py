# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	Flags: "U32"

@dataclass
class RequestData:
	ItemType: "U32"

@dataclass
class Data:
	X: "U32"
	Y: "U32"
	ID: "LLUUID"
	Extra: "S32"
	Extra2: "S32"
	Name: "Variable 1"


class MapItemReply(Message):

	absolute_id = 4294902171 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.RequestData = RequestData(*((None,)*1))
		self.Data = [Data(*((None,)*6))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
		self.RequestData = RequestData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Data = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","uuid","signed int32","signed int32","variable1",],remaining_bytes)
			self.Data.append(Data(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: MapItemReply, 
Message Absolute ID: 4294902171
Blocks:
{self.AgentData}
{self.RequestData}
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32",],self.AgentData.AgentID,self.AgentData.Flags)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.RequestData.ItemType)

		blocks_count = len(self.Data)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","uuid","signed int32","signed int32","variable1",],self.Data[i].X,self.Data[i].Y,self.Data[i].ID,self.Data[i].Extra,self.Data[i].Extra2,self.Data[i].Name)

		return output