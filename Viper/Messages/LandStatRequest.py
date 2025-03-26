# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class RequestData:
	ReportType: "U32"
	RequestFlags: "U32"
	Filter: "Variable 1"
	ParcelLocalID: "S32"


class LandStatRequest(Message):

	absolute_id = 4294902181 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.RequestData = RequestData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","variable1","signed int32",],remaining_bytes)
		self.RequestData = RequestData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: LandStatRequest, 
Message Absolute ID: 4294902181
Blocks:
{self.AgentData}
{self.RequestData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","variable1","signed int32",],self.RequestData.ReportType,self.RequestData.RequestFlags,self.RequestData.Filter,self.RequestData.ParcelLocalID)

		return output