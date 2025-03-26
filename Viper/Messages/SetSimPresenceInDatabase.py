# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class SimData:
	RegionID: "LLUUID"
	HostName: "Variable 1"
	GridX: "U32"
	GridY: "U32"
	PID: "S32"
	AgentCount: "S32"
	TimeToLive: "S32"
	Status: "Variable 1"


class SetSimPresenceInDatabase(Message):

	absolute_id = 4294901783 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.SimData = SimData(*((None,)*8))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","unsigned int32","unsigned int32","signed int32","signed int32","signed int32","variable1",],remaining_bytes)
		self.SimData = SimData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SetSimPresenceInDatabase, 
Message Absolute ID: 4294901783
Blocks:
{self.SimData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","unsigned int32","unsigned int32","signed int32","signed int32","signed int32","variable1",],self.SimData.RegionID,self.SimData.HostName,self.SimData.GridX,self.SimData.GridY,self.SimData.PID,self.SimData.AgentCount,self.SimData.TimeToLive,self.SimData.Status)

		return output