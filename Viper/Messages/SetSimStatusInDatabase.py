# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Data:
	RegionID: "LLUUID"
	HostName: "Variable 1"
	X: "S32"
	Y: "S32"
	PID: "S32"
	AgentCount: "S32"
	TimeToLive: "S32"
	Status: "Variable 1"


class SetSimStatusInDatabase(Message):

	absolute_id = 4294901782 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = Data(*((None,)*8))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","signed int32","signed int32","signed int32","signed int32","signed int32","variable1",],remaining_bytes)
		self.Data = Data(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SetSimStatusInDatabase, 
Message Absolute ID: 4294901782
Blocks:
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","signed int32","signed int32","signed int32","signed int32","signed int32","variable1",],self.Data.RegionID,self.Data.HostName,self.Data.X,self.Data.Y,self.Data.PID,self.Data.AgentCount,self.Data.TimeToLive,self.Data.Status)

		return output