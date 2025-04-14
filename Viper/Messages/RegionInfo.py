# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class RegionInfo:
	SimName: "Variable 1"
	EstateID: "U32"
	ParentEstateID: "U32"
	RegionFlags: "U32"
	SimAccess: "U8"
	MaxAgents: "U8"
	BillableFactor: "F32"
	ObjectBonusFactor: "F32"
	WaterHeight: "F32"
	TerrainRaiseLimit: "F32"
	TerrainLowerLimit: "F32"
	PricePerMeter: "S32"
	RedirectGridX: "S32"
	RedirectGridY: "S32"
	UseEstateSun: "BOOL"
	SunHour: "F32"
REGIONINFO = RegionInfo

@dataclass
class RegionInfo2:
	ProductSKU: "Variable 1"
	ProductName: "Variable 1"
	MaxAgents32: "U32"
	HardMaxAgents: "U32"
	HardMaxObjects: "U32"
REGIONINFO2 = RegionInfo2

@dataclass
class RegionInfo3:
	RegionFlagsExtended: "U64"
REGIONINFO3 = RegionInfo3

@dataclass
class RegionInfo5:
	ChatWhisperRange: "F32"
	ChatNormalRange: "F32"
	ChatShoutRange: "F32"
	ChatWhisperOffset: "F32"
	ChatNormalOffset: "F32"
	ChatShoutOffset: "F32"
	ChatFlags: "U32"
REGIONINFO5 = RegionInfo5

@dataclass
class CombatSettings:
	CombatFlags: "U32"
	OnDeath: "U8"
	DamageThrottle: "F32"
	RegenerationRate: "F32"
	InvulnerabilyTime: "F32"
	DamageLimit: "F32"
COMBATSETTINGS = CombatSettings


class RegionInfo(Message):

	absolute_id = 4294901902 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.AgentData = AGENTDATA(*((None,)*2))

		self.RegionInfo = REGIONINFO(*((None,)*16))

		self.RegionInfo2 = REGIONINFO2(*((None,)*5))

		self.RegionInfo3 = [REGIONINFO3(*((None,)*1))]

		self.RegionInfo5 = [REGIONINFO5(*((None,)*7))]

		self.CombatSettings = [COMBATSETTINGS(*((None,)*6))]

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","unsigned int32","unsigned int32","unsigned int32","unsigned byte","unsigned byte","float","float","float","float","float","signed int32","signed int32","signed int32","unsigned byte","float",],remaining_bytes)
		self.RegionInfo = REGIONINFO(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","variable1","unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
		self.RegionInfo2 = REGIONINFO2(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.RegionInfo3 = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64",],remaining_bytes)
			self.RegionInfo3.append(REGIONINFO3(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.RegionInfo5 = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["float","float","float","float","float","float","unsigned int32",],remaining_bytes)
			self.RegionInfo5.append(REGIONINFO5(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.CombatSettings = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned byte","float","float","float","float",],remaining_bytes)
			self.CombatSettings.append(COMBATSETTINGS(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: RegionInfo, Message Absolute ID: 4294901902, Blocks: {self.AgentData},{self.RegionInfo},{self.RegionInfo2},{self.RegionInfo3},{self.RegionInfo5},{self.CombatSettings}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","unsigned int32","unsigned int32","unsigned int32","unsigned byte","unsigned byte","float","float","float","float","float","signed int32","signed int32","signed int32","unsigned byte","float",],self.RegionInfo.SimName,self.RegionInfo.EstateID,self.RegionInfo.ParentEstateID,self.RegionInfo.RegionFlags,self.RegionInfo.SimAccess,self.RegionInfo.MaxAgents,self.RegionInfo.BillableFactor,self.RegionInfo.ObjectBonusFactor,self.RegionInfo.WaterHeight,self.RegionInfo.TerrainRaiseLimit,self.RegionInfo.TerrainLowerLimit,self.RegionInfo.PricePerMeter,self.RegionInfo.RedirectGridX,self.RegionInfo.RedirectGridY,self.RegionInfo.UseEstateSun,self.RegionInfo.SunHour)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","variable1","unsigned int32","unsigned int32","unsigned int32",],self.RegionInfo2.ProductSKU,self.RegionInfo2.ProductName,self.RegionInfo2.MaxAgents32,self.RegionInfo2.HardMaxAgents,self.RegionInfo2.HardMaxObjects)

		blocks_count = len(self.RegionInfo3)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64",],self.RegionInfo3[i].RegionFlagsExtended)

		blocks_count = len(self.RegionInfo5)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["float","float","float","float","float","float","unsigned int32",],self.RegionInfo5[i].ChatWhisperRange,self.RegionInfo5[i].ChatNormalRange,self.RegionInfo5[i].ChatShoutRange,self.RegionInfo5[i].ChatWhisperOffset,self.RegionInfo5[i].ChatNormalOffset,self.RegionInfo5[i].ChatShoutOffset,self.RegionInfo5[i].ChatFlags)

		blocks_count = len(self.CombatSettings)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned byte","float","float","float","float",],self.CombatSettings[i].CombatFlags,self.CombatSettings[i].OnDeath,self.CombatSettings[i].DamageThrottle,self.CombatSettings[i].RegenerationRate,self.CombatSettings[i].InvulnerabilyTime,self.CombatSettings[i].DamageLimit)

		return output