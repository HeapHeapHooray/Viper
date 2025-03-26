# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class SimulatorInfo:
	RegionID: "LLUUID"
	SimName: "Variable 1"
	EstateID: "U32"
	SimAccess: "U8"


class UpdateSimulator(Message):

	absolute_id = 4294901777 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.SimulatorInfo = SimulatorInfo(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","unsigned int32","unsigned byte",],remaining_bytes)
		self.SimulatorInfo = SimulatorInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: UpdateSimulator, 
Message Absolute ID: 4294901777
Blocks:
{self.SimulatorInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","unsigned int32","unsigned byte",],self.SimulatorInfo.RegionID,self.SimulatorInfo.SimName,self.SimulatorInfo.EstateID,self.SimulatorInfo.SimAccess)

		return output