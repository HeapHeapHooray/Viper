# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class SoundData:
	SoundID: "LLUUID"
	OwnerID: "LLUUID"
	ObjectID: "LLUUID"
	ParentID: "LLUUID"
	Handle: "U64"
	Position: "LLVector3"
	Gain: "F32"


class SoundTrigger(Message):

	absolute_id = 29 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.SoundData = SoundData(*((None,)*7))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","uuid","unsigned int64","vector3","float",],remaining_bytes)
		self.SoundData = SoundData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SoundTrigger, 
Message Absolute ID: 29
Blocks:
{self.SoundData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","uuid","unsigned int64","vector3","float",],self.SoundData.SoundID,self.SoundData.OwnerID,self.SoundData.ObjectID,self.SoundData.ParentID,self.SoundData.Handle,self.SoundData.Position,self.SoundData.Gain)

		return output