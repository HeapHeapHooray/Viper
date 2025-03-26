# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	QueryID: "LLUUID"

@dataclass
class TransactionData:
	TransactionID: "LLUUID"

@dataclass
class QueryData:
	QueryText: "Variable 1"
	QueryFlags: "U32"
	Category: "S8"
	SimName: "Variable 1"


class PlacesQuery(Message):

	absolute_id = 4294901789 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.TransactionData = TransactionData(*((None,)*1))
		self.QueryData = QueryData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.TransactionData = TransactionData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","unsigned int32","signed byte","variable1",],remaining_bytes)
		self.QueryData = QueryData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: PlacesQuery, 
Message Absolute ID: 4294901789
Blocks:
{self.AgentData}
{self.TransactionData}
{self.QueryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.QueryID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.TransactionData.TransactionID)

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","unsigned int32","signed byte","variable1",],self.QueryData.QueryText,self.QueryData.QueryFlags,self.QueryData.Category,self.QueryData.SimName)

		return output