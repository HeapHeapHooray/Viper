# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Info:
	AgentID: "LLUUID"
	LocationID: "U32"
	SimIP: "IPADDR"
	SimPort: "IPPORT"
	RegionHandle: "U64"
	SeedCapability: "Variable 2"
	SimAccess: "U8"
	TeleportFlags: "U32"


class TeleportFinish(Message):

	absolute_id = 4294901829 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Info = Info(*((None,)*8))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32","unsigned int32","unsigned int16","unsigned int64","variable2","unsigned byte","unsigned int32",],remaining_bytes)
		self.Info = Info(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TeleportFinish, 
Message Absolute ID: 4294901829
Blocks:
{self.Info}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32","unsigned int32","unsigned int16","unsigned int64","variable2","unsigned byte","unsigned int32",],self.Info.AgentID,self.Info.LocationID,self.Info.SimIP,self.Info.SimPort,self.Info.RegionHandle,self.Info.SeedCapability,self.Info.SimAccess,self.Info.TeleportFlags)

		return output