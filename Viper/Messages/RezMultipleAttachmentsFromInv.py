# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class HeaderData:
	CompoundMsgID: "LLUUID"
	TotalObjects: "U8"
	FirstDetachAll: "BOOL"

@dataclass
class ObjectData:
	ItemID: "LLUUID"
	OwnerID: "LLUUID"
	AttachmentPt: "U8"
	ItemFlags: "U32"
	GroupMask: "U32"
	EveryoneMask: "U32"
	NextOwnerMask: "U32"
	Name: "Variable 1"
	Description: "Variable 1"


class RezMultipleAttachmentsFromInv(Message):

	absolute_id = 4294902156 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.HeaderData = HeaderData(*((None,)*3))
		self.ObjectData = [ObjectData(*((None,)*9))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte","unsigned byte",],remaining_bytes)
		self.HeaderData = HeaderData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte","unsigned int32","unsigned int32","unsigned int32","unsigned int32","variable1","variable1",],remaining_bytes)
			self.ObjectData.append(ObjectData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: RezMultipleAttachmentsFromInv, 
Message Absolute ID: 4294902156
Blocks:
{self.AgentData}
{self.HeaderData}
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte","unsigned byte",],self.HeaderData.CompoundMsgID,self.HeaderData.TotalObjects,self.HeaderData.FirstDetachAll)

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte","unsigned int32","unsigned int32","unsigned int32","unsigned int32","variable1","variable1",],self.ObjectData[i].ItemID,self.ObjectData[i].OwnerID,self.ObjectData[i].AttachmentPt,self.ObjectData[i].ItemFlags,self.ObjectData[i].GroupMask,self.ObjectData[i].EveryoneMask,self.ObjectData[i].NextOwnerMask,self.ObjectData[i].Name,self.ObjectData[i].Description)

		return output