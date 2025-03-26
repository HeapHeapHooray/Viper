# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	TransactionID: "LLUUID"

@dataclass
class MethodData:
	Method: "Variable 1"
	Invoice: "LLUUID"

@dataclass
class ParamList:
	Parameter: "Variable 2"


class LargeGenericMessage(Message):

	absolute_id = 4294902190 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.MethodData = MethodData(*((None,)*2))
		self.ParamList = [ParamList(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","uuid",],remaining_bytes)
		self.MethodData = MethodData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ParamList = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
			self.ParamList.append(ParamList(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: LargeGenericMessage, 
Message Absolute ID: 4294902190
Blocks:
{self.AgentData}
{self.MethodData}
{self.ParamList}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.TransactionID)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","uuid",],self.MethodData.Method,self.MethodData.Invoice)

		blocks_count = len(self.ParamList)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.ParamList[i].Parameter)

		return output