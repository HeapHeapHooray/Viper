# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class SimulatorPublicHostBlock:
	Port: "IPPORT"
	SimulatorIP: "IPADDR"
	GridX: "U32"
	GridY: "U32"
SIMULATORPUBLICHOSTBLOCK = SimulatorPublicHostBlock

@dataclass
class NeighborBlock:
	IP: "IPADDR"
	Port: "IPPORT"
NEIGHBORBLOCK = NeighborBlock

@dataclass
class SimulatorBlock:
	SimName: "Variable 1"
	SimAccess: "U8"
	RegionFlags: "U32"
	RegionID: "LLUUID"
	EstateID: "U32"
	ParentEstateID: "U32"
SIMULATORBLOCK = SimulatorBlock

@dataclass
class TelehubBlock:
	HasTelehub: "BOOL"
	TelehubPos: "LLVector3"
TELEHUBBLOCK = TelehubBlock


class SimulatorPresentAtLocation(Message):

	absolute_id = 4294901771 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.SimulatorPublicHostBlock = SIMULATORPUBLICHOSTBLOCK(*((None,)*4))

		self.NeighborBlock = []
		for i in range(4):
			self.NeighborBlock.append(NEIGHBORBLOCK(*((None,)*2)))

		self.SimulatorBlock = SIMULATORBLOCK(*((None,)*6))

		self.TelehubBlock = [TELEHUBBLOCK(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int16","unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
		self.SimulatorPublicHostBlock = SIMULATORPUBLICHOSTBLOCK(*unpacked_data)

		blocks_count = 4 # -- Fixed/constant Blocks length of 4. 

		self.NeighborBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int16",],remaining_bytes)
			self.NeighborBlock.append(NEIGHBORBLOCK(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","unsigned byte","unsigned int32","uuid","unsigned int32","unsigned int32",],remaining_bytes)
		self.SimulatorBlock = SIMULATORBLOCK(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.TelehubBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","vector3",],remaining_bytes)
			self.TelehubBlock.append(TELEHUBBLOCK(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: SimulatorPresentAtLocation, Message Absolute ID: 4294901771, Blocks: {self.SimulatorPublicHostBlock},{self.NeighborBlock},{self.SimulatorBlock},{self.TelehubBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int16","unsigned int32","unsigned int32","unsigned int32",],self.SimulatorPublicHostBlock.Port,self.SimulatorPublicHostBlock.SimulatorIP,self.SimulatorPublicHostBlock.GridX,self.SimulatorPublicHostBlock.GridY)

		blocks_count = 4

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int16",],self.NeighborBlock[i].IP,self.NeighborBlock[i].Port)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","unsigned byte","unsigned int32","uuid","unsigned int32","unsigned int32",],self.SimulatorBlock.SimName,self.SimulatorBlock.SimAccess,self.SimulatorBlock.RegionFlags,self.SimulatorBlock.RegionID,self.SimulatorBlock.EstateID,self.SimulatorBlock.ParentEstateID)

		blocks_count = len(self.TelehubBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","vector3",],self.TelehubBlock[i].HasTelehub,self.TelehubBlock[i].TelehubPos)

		return output