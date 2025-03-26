# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class MethodData:
	Method: "Variable 1"
	Invoice: "LLUUID"
	Digest: "Fixed 32"

@dataclass
class ParamList:
	Parameter: "Variable 1"


class SystemMessage(Message):

	absolute_id = 4294902164 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.MethodData = MethodData(*((None,)*3))
		self.ParamList = [ParamList(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","uuid","fixed32",],remaining_bytes)
		self.MethodData = MethodData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ParamList = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1",],remaining_bytes)
			self.ParamList.append(ParamList(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: SystemMessage, 
Message Absolute ID: 4294902164
Blocks:
{self.MethodData}
{self.ParamList}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","uuid","fixed32",],self.MethodData.Method,self.MethodData.Invoice,self.MethodData.Digest)

		blocks_count = len(self.ParamList)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable1",],self.ParamList[i].Parameter)

		return output