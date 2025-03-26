# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class StartLocationData:
	AgentID: "LLUUID"
	RegionID: "LLUUID"
	LocationID: "U32"
	RegionHandle: "U64"
	LocationPos: "LLVector3"
	LocationLookAt: "LLVector3"


class SetStartLocation(Message):

	absolute_id = 4294902085 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.StartLocationData = StartLocationData(*((None,)*6))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned int64","vector3","vector3",],remaining_bytes)
		self.StartLocationData = StartLocationData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SetStartLocation, 
Message Absolute ID: 4294902085
Blocks:
{self.StartLocationData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned int64","vector3","vector3",],self.StartLocationData.AgentID,self.StartLocationData.RegionID,self.StartLocationData.LocationID,self.StartLocationData.RegionHandle,self.StartLocationData.LocationPos,self.StartLocationData.LocationLookAt)

		return output