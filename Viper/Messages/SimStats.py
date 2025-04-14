# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class Region:
	RegionX: "U32"
	RegionY: "U32"
	RegionFlags: "U32"
	ObjectCapacity: "U32"
REGION = Region

@dataclass
class Stat:
	StatID: "U32"
	StatValue: "F32"
STAT = Stat

@dataclass
class PidStat:
	PID: "S32"
PIDSTAT = PidStat

@dataclass
class RegionInfo:
	RegionFlagsExtended: "U64"
REGIONINFO = RegionInfo


class SimStats(Message):

	absolute_id = 4294901900 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Region = REGION(*((None,)*4))
		self.Stat = [STAT(*((None,)*2))]
		self.PidStat = PIDSTAT(*((None,)*1))
		self.RegionInfo = [REGIONINFO(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
		self.Region = REGION(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Stat = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","float",],remaining_bytes)
			self.Stat.append(STAT(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32",],remaining_bytes)
		self.PidStat = PIDSTAT(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.RegionInfo = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64",],remaining_bytes)
			self.RegionInfo.append(REGIONINFO(*unpacked_data))


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