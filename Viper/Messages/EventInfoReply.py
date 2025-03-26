# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"

@dataclass
class EventData:
	EventID: "U32"
	Creator: "Variable 1"
	Name: "Variable 1"
	Category: "Variable 1"
	Desc: "Variable 2"
	Date: "Variable 1"
	DateUTC: "U32"
	Duration: "U32"
	Cover: "U32"
	Amount: "U32"
	SimName: "Variable 1"
	GlobalPos: "LLVector3d"
	EventFlags: "U32"


class EventInfoReply(Message):

	absolute_id = 4294901940 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*1))
		self.EventData = EventData(*((None,)*13))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","variable1","variable1","variable1","variable2","variable1","unsigned int32","unsigned int32","unsigned int32","unsigned int32","variable1","vector3d","unsigned int32",],remaining_bytes)
		self.EventData = EventData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: EventInfoReply, 
Message Absolute ID: 4294901940
Blocks:
{self.AgentData}
{self.EventData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","variable1","variable1","variable1","variable2","variable1","unsigned int32","unsigned int32","unsigned int32","unsigned int32","variable1","vector3d","unsigned int32",],self.EventData.EventID,self.EventData.Creator,self.EventData.Name,self.EventData.Category,self.EventData.Desc,self.EventData.Date,self.EventData.DateUTC,self.EventData.Duration,self.EventData.Cover,self.EventData.Amount,self.EventData.SimName,self.EventData.GlobalPos,self.EventData.EventFlags)

		return output