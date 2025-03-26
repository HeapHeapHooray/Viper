# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	QueryID: "LLUUID"

@dataclass
class TransactionData:
	TransactionID: "LLUUID"

@dataclass
class QueryData:
	OwnerID: "LLUUID"
	Name: "Variable 1"
	Desc: "Variable 1"
	ActualArea: "S32"
	BillableArea: "S32"
	Flags: "U8"
	GlobalX: "F32"
	GlobalY: "F32"
	GlobalZ: "F32"
	SimName: "Variable 1"
	SnapshotID: "LLUUID"
	Dwell: "F32"
	Price: "S32"


class PlacesReply(Message):

	absolute_id = 4294901790 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.TransactionData = TransactionData(*((None,)*1))
		self.QueryData = [QueryData(*((None,)*13))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.TransactionData = TransactionData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.QueryData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","variable1","signed int32","signed int32","unsigned byte","float","float","float","variable1","uuid","float","signed int32",],remaining_bytes)
			self.QueryData.append(QueryData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: PlacesReply, 
Message Absolute ID: 4294901790
Blocks:
{self.AgentData}
{self.TransactionData}
{self.QueryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.QueryID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.TransactionData.TransactionID)

		blocks_count = len(self.QueryData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","variable1","signed int32","signed int32","unsigned byte","float","float","float","variable1","uuid","float","signed int32",],self.QueryData[i].OwnerID,self.QueryData[i].Name,self.QueryData[i].Desc,self.QueryData[i].ActualArea,self.QueryData[i].BillableArea,self.QueryData[i].Flags,self.QueryData[i].GlobalX,self.QueryData[i].GlobalY,self.QueryData[i].GlobalZ,self.QueryData[i].SimName,self.QueryData[i].SnapshotID,self.QueryData[i].Dwell,self.QueryData[i].Price)

		return output