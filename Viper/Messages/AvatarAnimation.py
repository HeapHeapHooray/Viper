# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Sender:
	ID: "LLUUID"

@dataclass
class AnimationList:
	AnimID: "LLUUID"
	AnimSequenceID: "S32"

@dataclass
class AnimationSourceList:
	ObjectID: "LLUUID"

@dataclass
class PhysicalAvatarEventList:
	TypeData: "Variable 1"


class AvatarAnimation(Message):

	absolute_id = 20 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Sender = Sender(*((None,)*1))
		self.AnimationList = [AnimationList(*((None,)*2))]
		self.AnimationSourceList = [AnimationSourceList(*((None,)*1))]
		self.PhysicalAvatarEventList = [PhysicalAvatarEventList(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.Sender = Sender(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AnimationList = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int32",],remaining_bytes)
			self.AnimationList.append(AnimationList(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AnimationSourceList = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.AnimationSourceList.append(AnimationSourceList(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.PhysicalAvatarEventList = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1",],remaining_bytes)
			self.PhysicalAvatarEventList.append(PhysicalAvatarEventList(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarAnimation, 
Message Absolute ID: 20
Blocks:
{self.Sender}
{self.AnimationList}
{self.AnimationSourceList}
{self.PhysicalAvatarEventList}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.Sender.ID)

		blocks_count = len(self.AnimationList)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int32",],self.AnimationList[i].AnimID,self.AnimationList[i].AnimSequenceID)

		blocks_count = len(self.AnimationSourceList)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AnimationSourceList[i].ObjectID)

		blocks_count = len(self.PhysicalAvatarEventList)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable1",],self.PhysicalAvatarEventList[i].TypeData)

		return output