# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class RequestImage:
	Image: "LLUUID"
	DiscardLevel: "S8"
	DownloadPriority: "F32"
	Packet: "U32"
	Type: "U8"


class RequestImage(Message):

	absolute_id = 8 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.RequestImage = [RequestImage(*((None,)*5))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.RequestImage = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed byte","float","unsigned int32","unsigned byte",],remaining_bytes)
			self.RequestImage.append(RequestImage(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: RequestImage, 
Message Absolute ID: 8
Blocks:
{self.AgentData}
{self.RequestImage}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		blocks_count = len(self.RequestImage)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed byte","float","unsigned int32","unsigned byte",],self.RequestImage[i].Image,self.RequestImage[i].DiscardLevel,self.RequestImage[i].DownloadPriority,self.RequestImage[i].Packet,self.RequestImage[i].Type)

		return output