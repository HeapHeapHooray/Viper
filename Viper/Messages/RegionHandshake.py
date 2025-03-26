# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class RegionInfo:
	RegionFlags: "U32"
	SimAccess: "U8"
	SimName: "Variable 1"
	SimOwner: "LLUUID"
	IsEstateManager: "BOOL"
	WaterHeight: "F32"
	BillableFactor: "F32"
	CacheID: "LLUUID"
	TerrainBase0: "LLUUID"
	TerrainBase1: "LLUUID"
	TerrainBase2: "LLUUID"
	TerrainBase3: "LLUUID"
	TerrainDetail0: "LLUUID"
	TerrainDetail1: "LLUUID"
	TerrainDetail2: "LLUUID"
	TerrainDetail3: "LLUUID"
	TerrainStartHeight00: "F32"
	TerrainStartHeight01: "F32"
	TerrainStartHeight10: "F32"
	TerrainStartHeight11: "F32"
	TerrainHeightRange00: "F32"
	TerrainHeightRange01: "F32"
	TerrainHeightRange10: "F32"
	TerrainHeightRange11: "F32"

@dataclass
class RegionInfo2:
	RegionID: "LLUUID"

@dataclass
class RegionInfo3:
	CPUClassID: "S32"
	CPURatio: "S32"
	ColoName: "Variable 1"
	ProductSKU: "Variable 1"
	ProductName: "Variable 1"

@dataclass
class RegionInfo4:
	RegionFlagsExtended: "U64"
	RegionProtocols: "U64"


class RegionHandshake(Message):

	absolute_id = 4294901908 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.RegionInfo = RegionInfo(*((None,)*24))
		self.RegionInfo2 = RegionInfo2(*((None,)*1))
		self.RegionInfo3 = RegionInfo3(*((None,)*5))
		self.RegionInfo4 = [RegionInfo4(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned byte","variable1","uuid","unsigned byte","float","float","uuid","uuid","uuid","uuid","uuid","uuid","uuid","uuid","uuid","float","float","float","float","float","float","float","float",],remaining_bytes)
		self.RegionInfo = RegionInfo(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.RegionInfo2 = RegionInfo2(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","signed int32","variable1","variable1","variable1",],remaining_bytes)
		self.RegionInfo3 = RegionInfo3(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.RegionInfo4 = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","unsigned int64",],remaining_bytes)
			self.RegionInfo4.append(RegionInfo4(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: RegionHandshake, 
Message Absolute ID: 4294901908
Blocks:
{self.RegionInfo}
{self.RegionInfo2}
{self.RegionInfo3}
{self.RegionInfo4}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned byte","variable1","uuid","unsigned byte","float","float","uuid","uuid","uuid","uuid","uuid","uuid","uuid","uuid","uuid","float","float","float","float","float","float","float","float",],self.RegionInfo.RegionFlags,self.RegionInfo.SimAccess,self.RegionInfo.SimName,self.RegionInfo.SimOwner,self.RegionInfo.IsEstateManager,self.RegionInfo.WaterHeight,self.RegionInfo.BillableFactor,self.RegionInfo.CacheID,self.RegionInfo.TerrainBase0,self.RegionInfo.TerrainBase1,self.RegionInfo.TerrainBase2,self.RegionInfo.TerrainBase3,self.RegionInfo.TerrainDetail0,self.RegionInfo.TerrainDetail1,self.RegionInfo.TerrainDetail2,self.RegionInfo.TerrainDetail3,self.RegionInfo.TerrainStartHeight00,self.RegionInfo.TerrainStartHeight01,self.RegionInfo.TerrainStartHeight10,self.RegionInfo.TerrainStartHeight11,self.RegionInfo.TerrainHeightRange00,self.RegionInfo.TerrainHeightRange01,self.RegionInfo.TerrainHeightRange10,self.RegionInfo.TerrainHeightRange11)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.RegionInfo2.RegionID)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","signed int32","variable1","variable1","variable1",],self.RegionInfo3.CPUClassID,self.RegionInfo3.CPURatio,self.RegionInfo3.ColoName,self.RegionInfo3.ProductSKU,self.RegionInfo3.ProductName)

		blocks_count = len(self.RegionInfo4)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","unsigned int64",],self.RegionInfo4[i].RegionFlagsExtended,self.RegionInfo4[i].RegionProtocols)

		return output