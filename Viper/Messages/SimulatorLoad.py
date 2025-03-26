# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class SimulatorLoad:
	TimeDilation: "F32"
	AgentCount: "S32"
	CanAcceptAgents: "BOOL"

@dataclass
class AgentList:
	CircuitCode: "U32"
	X: "U8"
	Y: "U8"


class SimulatorLoad(Message):

	absolute_id = 4294901772 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.SimulatorLoad = SimulatorLoad(*((None,)*3))
		self.AgentList = [AgentList(*((None,)*3))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["float","signed int32","unsigned byte",],remaining_bytes)
		self.SimulatorLoad = SimulatorLoad(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AgentList = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned byte","unsigned byte",],remaining_bytes)
			self.AgentList.append(AgentList(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: SimulatorLoad, 
Message Absolute ID: 4294901772
Blocks:
{self.SimulatorLoad}
{self.AgentList}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["float","signed int32","unsigned byte",],self.SimulatorLoad.TimeDilation,self.SimulatorLoad.AgentCount,self.SimulatorLoad.CanAcceptAgents)

		blocks_count = len(self.AgentList)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned byte","unsigned byte",],self.AgentList[i].CircuitCode,self.AgentList[i].X,self.AgentList[i].Y)

		return output