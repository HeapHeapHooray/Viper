# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	ObjectID: "LLUUID"
	Gain: "F32"


class AttachedSoundGainChange(Message):

	absolute_id = 65294 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = DataBlock(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","float",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AttachedSoundGainChange, 
Message Absolute ID: 65294
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","float",],self.DataBlock.ObjectID,self.DataBlock.Gain)

		return output