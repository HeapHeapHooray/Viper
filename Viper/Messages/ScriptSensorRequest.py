# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Requester:
	SourceID: "LLUUID"
	RequestID: "LLUUID"
	SearchID: "LLUUID"
	SearchPos: "LLVector3"
	SearchDir: "LLQuaternion"
	SearchName: "Variable 1"
	Type: "S32"
	Range: "F32"
	Arc: "F32"
	RegionHandle: "U64"
	SearchRegions: "U8"


class ScriptSensorRequest(Message):

	absolute_id = 4294902007 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Requester = Requester(*((None,)*11))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","vector3","unit_quaternion","variable1","signed int32","float","float","unsigned int64","unsigned byte",],remaining_bytes)
		self.Requester = Requester(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ScriptSensorRequest, 
Message Absolute ID: 4294902007
Blocks:
{self.Requester}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","vector3","unit_quaternion","variable1","signed int32","float","float","unsigned int64","unsigned byte",],self.Requester.SourceID,self.Requester.RequestID,self.Requester.SearchID,self.Requester.SearchPos,self.Requester.SearchDir,self.Requester.SearchName,self.Requester.Type,self.Requester.Range,self.Requester.Arc,self.Requester.RegionHandle,self.Requester.SearchRegions)

		return output