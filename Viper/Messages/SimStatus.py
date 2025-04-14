# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class SimStatus:
	CanAcceptAgents: "BOOL"
	CanAcceptTasks: "BOOL"
SIMSTATUS = SimStatus

@dataclass
class SimFlags:
	Flags: "U64"
SIMFLAGS = SimFlags


class SimStatus(Message):

	absolute_id = 65292 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.SimStatus = SIMSTATUS(*((None,)*2))
		self.SimFlags = SIMFLAGS(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned byte",],remaining_bytes)
		self.SimStatus = SIMSTATUS(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64",],remaining_bytes)
		self.SimFlags = SIMFLAGS(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SimStatus, 
Message Absolute ID: 65292
Blocks:
{self.SimStatus}
{self.SimFlags}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned byte",],self.SimStatus.CanAcceptAgents,self.SimStatus.CanAcceptTasks)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64",],self.SimFlags.Flags)

		return output