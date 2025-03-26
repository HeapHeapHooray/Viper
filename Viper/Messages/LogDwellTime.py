# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class DwellInfo:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	Duration: "F32"
	SimName: "Variable 1"
	RegionX: "U32"
	RegionY: "U32"
	AvgAgentsInView: "U8"
	AvgViewerFPS: "U8"


class LogDwellTime(Message):

	absolute_id = 4294901778 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.DwellInfo = DwellInfo(*((None,)*8))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","float","variable1","unsigned int32","unsigned int32","unsigned byte","unsigned byte",],remaining_bytes)
		self.DwellInfo = DwellInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: LogDwellTime, 
Message Absolute ID: 4294901778
Blocks:
{self.DwellInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","float","variable1","unsigned int32","unsigned int32","unsigned byte","unsigned byte",],self.DwellInfo.AgentID,self.DwellInfo.SessionID,self.DwellInfo.Duration,self.DwellInfo.SimName,self.DwellInfo.RegionX,self.DwellInfo.RegionY,self.DwellInfo.AvgAgentsInView,self.DwellInfo.AvgViewerFPS)

		return output