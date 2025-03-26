# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class CircuitInfo:
	IP: "IPADDR"
	Port: "IPPORT"


class OpenCircuit(Message):

	absolute_id = 4294967292 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.CircuitInfo = CircuitInfo(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int16",],remaining_bytes)
		self.CircuitInfo = CircuitInfo(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: OpenCircuit, 
Message Absolute ID: 4294967292
Blocks:
{self.CircuitInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int16",],self.CircuitInfo.IP,self.CircuitInfo.Port)

		return output