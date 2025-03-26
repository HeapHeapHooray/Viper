# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Data:
	OwnerID: "LLUUID"
	IsGroupOwned: "BOOL"
	Count: "S32"
	OnlineStatus: "BOOL"


class ParcelObjectOwnersReply(Message):

	absolute_id = 4294901817 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = [Data(*((None,)*4))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Data = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte","signed int32","unsigned byte",],remaining_bytes)
			self.Data.append(Data(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelObjectOwnersReply, 
Message Absolute ID: 4294901817
Blocks:
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = len(self.Data)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte","signed int32","unsigned byte",],self.Data[i].OwnerID,self.Data[i].IsGroupOwned,self.Data[i].Count,self.Data[i].OnlineStatus)

		return output