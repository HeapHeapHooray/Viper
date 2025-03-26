# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Requester:
	SourceID: "LLUUID"

@dataclass
class SensedData:
	ObjectID: "LLUUID"
	OwnerID: "LLUUID"
	GroupID: "LLUUID"
	Position: "LLVector3"
	Velocity: "LLVector3"
	Rotation: "LLQuaternion"
	Name: "Variable 1"
	Type: "S32"
	Range: "F32"


class ScriptSensorReply(Message):

	absolute_id = 4294902008 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Requester = Requester(*((None,)*1))
		self.SensedData = [SensedData(*((None,)*9))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.Requester = Requester(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.SensedData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid","vector3","vector3","unit_quaternion","variable1","signed int32","float",],remaining_bytes)
			self.SensedData.append(SensedData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ScriptSensorReply, 
Message Absolute ID: 4294902008
Blocks:
{self.Requester}
{self.SensedData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.Requester.SourceID)

		blocks_count = len(self.SensedData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid","vector3","vector3","unit_quaternion","variable1","signed int32","float",],self.SensedData[i].ObjectID,self.SensedData[i].OwnerID,self.SensedData[i].GroupID,self.SensedData[i].Position,self.SensedData[i].Velocity,self.SensedData[i].Rotation,self.SensedData[i].Name,self.SensedData[i].Type,self.SensedData[i].Range)

		return output