# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class SimulatorInfo:
	Handle: "U64"
	IP: "IPADDR"
	Port: "IPPORT"


class EnableSimulator(Message):

	absolute_id = 4294901911 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.SimulatorInfo = SimulatorInfo(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","unsigned int32","unsigned int16",],remaining_bytes)
		self.SimulatorInfo = SimulatorInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: EnableSimulator, 
Message Absolute ID: 4294901911
Blocks:
{self.SimulatorInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","unsigned int32","unsigned int16",],self.SimulatorInfo.Handle,self.SimulatorInfo.IP,self.SimulatorInfo.Port)

		return output