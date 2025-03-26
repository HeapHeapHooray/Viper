# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TelehubBlock:
	ObjectID: "LLUUID"
	ObjectName: "Variable 1"
	TelehubPos: "LLVector3"
	TelehubRot: "LLQuaternion"

@dataclass
class SpawnPointBlock:
	SpawnPointPos: "LLVector3"


class TelehubInfo(Message):

	absolute_id = 4294901770 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TelehubBlock = TelehubBlock(*((None,)*4))
		self.SpawnPointBlock = [SpawnPointBlock(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","vector3","unit_quaternion",],remaining_bytes)
		self.TelehubBlock = TelehubBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.SpawnPointBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["vector3",],remaining_bytes)
			self.SpawnPointBlock.append(SpawnPointBlock(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: TelehubInfo, 
Message Absolute ID: 4294901770
Blocks:
{self.TelehubBlock}
{self.SpawnPointBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","vector3","unit_quaternion",],self.TelehubBlock.ObjectID,self.TelehubBlock.ObjectName,self.TelehubBlock.TelehubPos,self.TelehubBlock.TelehubRot)

		blocks_count = len(self.SpawnPointBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["vector3",],self.SpawnPointBlock[i].SpawnPointPos)

		return output