# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

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


class RezSingleAttachmentFromInv(Message):

	absolute_id = 4294902155 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.ObjectData = ObjectData(*((None,)*9))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte","unsigned int32","unsigned int32","unsigned int32","unsigned int32","variable1","variable1",],remaining_bytes)
		self.ObjectData = ObjectData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RezSingleAttachmentFromInv, 
Message Absolute ID: 4294902155
Blocks:
{self.AgentData}
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte","unsigned int32","unsigned int32","unsigned int32","unsigned int32","variable1","variable1",],self.ObjectData.ItemID,self.ObjectData.OwnerID,self.ObjectData.AttachmentPt,self.ObjectData.ItemFlags,self.ObjectData.GroupMask,self.ObjectData.EveryoneMask,self.ObjectData.NextOwnerMask,self.ObjectData.Name,self.ObjectData.Description)

		return output