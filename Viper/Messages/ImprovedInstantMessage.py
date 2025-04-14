# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class MessageBlock:
	FromGroup: "BOOL"
	ToAgentID: "LLUUID"
	ParentEstateID: "U32"
	RegionID: "LLUUID"
	Position: "LLVector3"
	Offline: "U8"
	Dialog: "U8"
	ID: "LLUUID"
	Timestamp: "U32"
	FromAgentName: "Variable 1"
	Message: "Variable 2"
	BinaryBucket: "Variable 2"
MESSAGEBLOCK = MessageBlock

@dataclass
class EstateBlock:
	EstateID: "U32"
ESTATEBLOCK = EstateBlock

@dataclass
class MetaData:
	Data: "Variable 2"
METADATA = MetaData


class ImprovedInstantMessage(Message):

	absolute_id = 4294902014 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*2))
		self.MessageBlock = MESSAGEBLOCK(*((None,)*12))
		self.EstateBlock = ESTATEBLOCK(*((None,)*1))
		self.MetaData = [METADATA(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","uuid","unsigned int32","uuid","vector3","unsigned byte","unsigned byte","uuid","unsigned int32","variable1","variable2","variable2",],remaining_bytes)
		self.MessageBlock = MESSAGEBLOCK(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
		self.EstateBlock = ESTATEBLOCK(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.MetaData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
			self.MetaData.append(METADATA(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ImprovedInstantMessage, 
Message Absolute ID: 4294902014
Blocks:
{self.AgentData}
{self.MessageBlock}
{self.EstateBlock}
{self.MetaData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","uuid","unsigned int32","uuid","vector3","unsigned byte","unsigned byte","uuid","unsigned int32","variable1","variable2","variable2",],self.MessageBlock.FromGroup,self.MessageBlock.ToAgentID,self.MessageBlock.ParentEstateID,self.MessageBlock.RegionID,self.MessageBlock.Position,self.MessageBlock.Offline,self.MessageBlock.Dialog,self.MessageBlock.ID,self.MessageBlock.Timestamp,self.MessageBlock.FromAgentName,self.MessageBlock.Message,self.MessageBlock.BinaryBucket)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.EstateBlock.EstateID)

		blocks_count = len(self.MetaData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.MetaData[i].Data)

		return output