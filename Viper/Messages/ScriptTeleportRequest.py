# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Data:
	ObjectName: "Variable 1"
	SimName: "Variable 1"
	SimPosition: "LLVector3"
	LookAt: "LLVector3"

@dataclass
class Options:
	Flags: "U32"


class ScriptTeleportRequest(Message):

	absolute_id = 4294901955 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = Data(*((None,)*4))
		self.Options = [Options(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","variable1","vector3","vector3",],remaining_bytes)
		self.Data = Data(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Options = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
			self.Options.append(Options(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ScriptTeleportRequest, 
Message Absolute ID: 4294901955
Blocks:
{self.Data}
{self.Options}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","variable1","vector3","vector3",],self.Data.ObjectName,self.Data.SimName,self.Data.SimPosition,self.Data.LookAt)

		blocks_count = len(self.Options)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.Options[i].Flags)

		return output