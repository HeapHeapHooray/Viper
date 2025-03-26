# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
	GroupID: "LLUUID"

@dataclass
class RezData:
	FromTaskID: "LLUUID"
	BypassRaycast: "U8"
	RayStart: "LLVector3"
	RayEnd: "LLVector3"
	RayTargetID: "LLUUID"
	RayEndIsIntersection: "BOOL"
	RezSelected: "BOOL"
	RemoveItem: "BOOL"
	ItemFlags: "U32"
	GroupMask: "U32"
	EveryoneMask: "U32"
	NextOwnerMask: "U32"

@dataclass
class NotecardData:
	NotecardItemID: "LLUUID"
	ObjectID: "LLUUID"

@dataclass
class InventoryData:
	ItemID: "LLUUID"


class RezObjectFromNotecard(Message):

	absolute_id = 4294902054 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*3))
		self.RezData = RezData(*((None,)*12))
		self.NotecardData = NotecardData(*((None,)*2))
		self.InventoryData = [InventoryData(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte","vector3","vector3","uuid","unsigned byte","unsigned byte","unsigned byte","unsigned int32","unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
		self.RezData = RezData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.NotecardData = NotecardData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.InventoryData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.InventoryData.append(InventoryData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: RezObjectFromNotecard, 
Message Absolute ID: 4294902054
Blocks:
{self.AgentData}
{self.RezData}
{self.NotecardData}
{self.InventoryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID,self.AgentData.GroupID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte","vector3","vector3","uuid","unsigned byte","unsigned byte","unsigned byte","unsigned int32","unsigned int32","unsigned int32","unsigned int32",],self.RezData.FromTaskID,self.RezData.BypassRaycast,self.RezData.RayStart,self.RezData.RayEnd,self.RezData.RayTargetID,self.RezData.RayEndIsIntersection,self.RezData.RezSelected,self.RezData.RemoveItem,self.RezData.ItemFlags,self.RezData.GroupMask,self.RezData.EveryoneMask,self.RezData.NextOwnerMask)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.NotecardData.NotecardItemID,self.NotecardData.ObjectID)

		blocks_count = len(self.InventoryData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.InventoryData[i].ItemID)

		return output