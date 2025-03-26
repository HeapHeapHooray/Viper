# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Data:
	AgentID: "LLUUID"
	SequenceID: "S32"
	Flags: "U32"
	LocalID: "S32"

@dataclass
class List:
	ID: "LLUUID"
	Time: "S32"
	Flags: "U32"


class ParcelAccessListReply(Message):

	absolute_id = 4294901976 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = Data(*((None,)*4))
		self.List = [List(*((None,)*3))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","unsigned int32","signed int32",],remaining_bytes)
		self.Data = Data(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.List = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32","unsigned int32",],remaining_bytes)
			self.List.append(List(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelAccessListReply, 
Message Absolute ID: 4294901976
Blocks:
{self.Data}
{self.List}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","unsigned int32","signed int32",],self.Data.AgentID,self.Data.SequenceID,self.Data.Flags,self.Data.LocalID)

		blocks_count = len(self.List)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32","unsigned int32",],self.List[i].ID,self.List[i].Time,self.List[i].Flags)

		return output