# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	IP: "IPADDR"
	StartTime: "U32"
	RunTime: "F32"
	SimFPS: "F32"
	FPS: "F32"
	AgentsInView: "U8"
	Ping: "F32"
	MetersTraveled: "F64"
	RegionsVisited: "S32"
	SysRAM: "U32"
	SysOS: "Variable 1"
	SysCPU: "Variable 1"
	SysGPU: "Variable 1"

@dataclass
class DownloadTotals:
	World: "U32"
	Objects: "U32"
	Textures: "U32"

@dataclass
class NetStats:
	Bytes: "U32"
	Packets: "U32"
	Compressed: "U32"
	Savings: "U32"

@dataclass
class FailStats:
	SendPacket: "U32"
	Dropped: "U32"
	Resent: "U32"
	FailedResends: "U32"
	OffCircuit: "U32"
	Invalid: "U32"

@dataclass
class MiscStats:
	Type: "U32"
	Value: "F64"


class ViewerStats(Message):

	absolute_id = 4294901891 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*15))
		self.DownloadTotals = DownloadTotals(*((None,)*3))
		self.NetStats = []
		for i in range(2):
			self.NetStats.append(NetStats(*((None,)*4)))
		self.FailStats = FailStats(*((None,)*6))
		self.MiscStats = [MiscStats(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned int32","float","float","float","unsigned byte","float","double","signed int32","unsigned int32","variable1","variable1","variable1",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
		self.DownloadTotals = DownloadTotals(*unpacked_data)

		blocks_count = 2 # -- Fixed/constant Blocks length of 2. 

		self.NetStats = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
			self.NetStats.append(NetStats(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
		self.FailStats = FailStats(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.MiscStats = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","double",],remaining_bytes)
			self.MiscStats.append(MiscStats(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ViewerStats, 
Message Absolute ID: 4294901891
Blocks:
{self.AgentData}
{self.DownloadTotals}
{self.NetStats}
{self.FailStats}
{self.MiscStats}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned int32","unsigned int32","float","float","float","unsigned byte","float","double","signed int32","unsigned int32","variable1","variable1","variable1",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.IP,self.AgentData.StartTime,self.AgentData.RunTime,self.AgentData.SimFPS,self.AgentData.FPS,self.AgentData.AgentsInView,self.AgentData.Ping,self.AgentData.MetersTraveled,self.AgentData.RegionsVisited,self.AgentData.SysRAM,self.AgentData.SysOS,self.AgentData.SysCPU,self.AgentData.SysGPU)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32",],self.DownloadTotals.World,self.DownloadTotals.Objects,self.DownloadTotals.Textures)

		blocks_count = 2

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32","unsigned int32",],self.NetStats[i].Bytes,self.NetStats[i].Packets,self.NetStats[i].Compressed,self.NetStats[i].Savings)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32","unsigned int32",],self.FailStats.SendPacket,self.FailStats.Dropped,self.FailStats.Resent,self.FailStats.FailedResends,self.FailStats.OffCircuit,self.FailStats.Invalid)

		blocks_count = len(self.MiscStats)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","double",],self.MiscStats[i].Type,self.MiscStats[i].Value)

		return output