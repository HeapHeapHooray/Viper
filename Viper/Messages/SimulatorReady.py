# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class SimulatorBlock:
	SimName: "Variable 1"
	SimAccess: "U8"
	RegionFlags: "U32"
	RegionID: "LLUUID"
	EstateID: "U32"
	ParentEstateID: "U32"

@dataclass
class TelehubBlock:
	HasTelehub: "BOOL"
	TelehubPos: "LLVector3"


class SimulatorReady(Message):

	absolute_id = 4294901769 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.SimulatorBlock = SimulatorBlock(*((None,)*6))
		self.TelehubBlock = TelehubBlock(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","unsigned byte","unsigned int32","uuid","unsigned int32","unsigned int32",],remaining_bytes)
		self.SimulatorBlock = SimulatorBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","vector3",],remaining_bytes)
		self.TelehubBlock = TelehubBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: SimulatorReady, 
Message Absolute ID: 4294901769
Blocks:
{self.SimulatorBlock}
{self.TelehubBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","unsigned byte","unsigned int32","uuid","unsigned int32","unsigned int32",],self.SimulatorBlock.SimName,self.SimulatorBlock.SimAccess,self.SimulatorBlock.RegionFlags,self.SimulatorBlock.RegionID,self.SimulatorBlock.EstateID,self.SimulatorBlock.ParentEstateID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","vector3",],self.TelehubBlock.HasTelehub,self.TelehubBlock.TelehubPos)

		return output