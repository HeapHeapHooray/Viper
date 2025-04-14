# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class XferID:
	ID: "U64"
	Packet: "U32"
XFERID = XferID

@dataclass
class DataPacket:
	Data: "Variable 2"
DATAPACKET = DataPacket


class SendXferPacket(Message):

	absolute_id = 18 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.XferID = XFERID(*((None,)*2))
		self.DataPacket = DATAPACKET(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","unsigned int32",],remaining_bytes)
		self.XferID = XFERID(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
		self.DataPacket = DATAPACKET(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SendXferPacket, 
Message Absolute ID: 18
Blocks:
{self.XferID}
{self.DataPacket}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","unsigned int32",],self.XferID.ID,self.XferID.Packet)

		output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.DataPacket.Data)

		return output