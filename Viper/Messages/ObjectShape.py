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
	ObjectLocalID: "U32"
	PathCurve: "U8"
	ProfileCurve: "U8"
	PathBegin: "U16"
	PathEnd: "U16"
	PathScaleX: "U8"
	PathScaleY: "U8"
	PathShearX: "U8"
	PathShearY: "U8"
	PathTwist: "S8"
	PathTwistBegin: "S8"
	PathRadiusOffset: "S8"
	PathTaperX: "S8"
	PathTaperY: "S8"
	PathRevolutions: "U8"
	PathSkew: "S8"
	ProfileBegin: "U16"
	ProfileEnd: "U16"
	ProfileHollow: "U16"


class ObjectShape(Message):

	absolute_id = 4294901858 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.ObjectData = [ObjectData(*((None,)*19))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ObjectData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned byte","unsigned byte","unsigned int16","unsigned int16","unsigned byte","unsigned byte","unsigned byte","unsigned byte","signed byte","signed byte","signed byte","signed byte","signed byte","unsigned byte","signed byte","unsigned int16","unsigned int16","unsigned int16",],remaining_bytes)
			self.ObjectData.append(ObjectData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ObjectShape, 
Message Absolute ID: 4294901858
Blocks:
{self.AgentData}
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		blocks_count = len(self.ObjectData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned byte","unsigned byte","unsigned int16","unsigned int16","unsigned byte","unsigned byte","unsigned byte","unsigned byte","signed byte","signed byte","signed byte","signed byte","signed byte","unsigned byte","signed byte","unsigned int16","unsigned int16","unsigned int16",],self.ObjectData[i].ObjectLocalID,self.ObjectData[i].PathCurve,self.ObjectData[i].ProfileCurve,self.ObjectData[i].PathBegin,self.ObjectData[i].PathEnd,self.ObjectData[i].PathScaleX,self.ObjectData[i].PathScaleY,self.ObjectData[i].PathShearX,self.ObjectData[i].PathShearY,self.ObjectData[i].PathTwist,self.ObjectData[i].PathTwistBegin,self.ObjectData[i].PathRadiusOffset,self.ObjectData[i].PathTaperX,self.ObjectData[i].PathTaperY,self.ObjectData[i].PathRevolutions,self.ObjectData[i].PathSkew,self.ObjectData[i].ProfileBegin,self.ObjectData[i].ProfileEnd,self.ObjectData[i].ProfileHollow)

		return output