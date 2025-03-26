# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	EndPointID: "LLUUID"
	Digest: "Fixed 32"


class CreateTrustedCircuit(Message):

	absolute_id = 4294902152 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = DataBlock(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","fixed32",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: CreateTrustedCircuit, 
Message Absolute ID: 4294902152
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","fixed32",],self.DataBlock.EndPointID,self.DataBlock.Digest)

		return output