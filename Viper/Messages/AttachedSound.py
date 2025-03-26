# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DataBlock:
	SoundID: "LLUUID"
	ObjectID: "LLUUID"
	OwnerID: "LLUUID"
	Gain: "F32"
	Flags: "U8"


class AttachedSound(Message):

	absolute_id = 65293 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DataBlock = DataBlock(*((None,)*5))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","float","unsigned byte",],remaining_bytes)
		self.DataBlock = DataBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AttachedSound, 
Message Absolute ID: 65293
Blocks:
{self.DataBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","float","unsigned byte",],self.DataBlock.SoundID,self.DataBlock.ObjectID,self.DataBlock.OwnerID,self.DataBlock.Gain,self.DataBlock.Flags)

		return output