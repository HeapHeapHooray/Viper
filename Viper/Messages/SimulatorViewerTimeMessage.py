# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TimeInfo:
	UsecSinceStart: "U64"
	SecPerDay: "U32"
	SecPerYear: "U32"
	SunDirection: "LLVector3"
	SunPhase: "F32"
	SunAngVelocity: "LLVector3"


class SimulatorViewerTimeMessage(Message):

	absolute_id = 4294901910 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TimeInfo = TimeInfo(*((None,)*6))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","unsigned int32","unsigned int32","vector3","float","vector3",],remaining_bytes)
		self.TimeInfo = TimeInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SimulatorViewerTimeMessage, 
Message Absolute ID: 4294901910
Blocks:
{self.TimeInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","unsigned int32","unsigned int32","vector3","float","vector3",],self.TimeInfo.UsecSinceStart,self.TimeInfo.SecPerDay,self.TimeInfo.SecPerYear,self.TimeInfo.SunDirection,self.TimeInfo.SunPhase,self.TimeInfo.SunAngVelocity)

		return output