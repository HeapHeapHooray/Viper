# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Region:
	RegionX: "U32"
	RegionY: "U32"
	RegionFlags: "U32"
	ObjectCapacity: "U32"

@dataclass
class Stat:
	StatID: "U32"
	StatValue: "F32"

@dataclass
class PidStat:
	PID: "S32"

@dataclass
class RegionInfo:
	RegionFlagsExtended: "U64"


class SimStats(Message):

	absolute_id = 4294901900 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Region = Region(*((None,)*4))
		self.Stat = [Stat(*((None,)*2))]
		self.PidStat = PidStat(*((None,)*1))
		self.RegionInfo = [RegionInfo(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
		self.Region = Region(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Stat = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","float",],remaining_bytes)
			self.Stat.append(Stat(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32",],remaining_bytes)
		self.PidStat = PidStat(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.RegionInfo = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64",],remaining_bytes)
			self.RegionInfo.append(RegionInfo(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: SimStats, 
Message Absolute ID: 4294901900
Blocks:
{self.Region}
{self.Stat}
{self.PidStat}
{self.RegionInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32","unsigned int32",],self.Region.RegionX,self.Region.RegionY,self.Region.RegionFlags,self.Region.ObjectCapacity)

		blocks_count = len(self.Stat)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","float",],self.Stat[i].StatID,self.Stat[i].StatValue)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32",],self.PidStat.PID)

		blocks_count = len(self.RegionInfo)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64",],self.RegionInfo[i].RegionFlagsExtended)

		return output