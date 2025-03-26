# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Sender:
	ID: "LLUUID"
	IsTrial: "BOOL"

@dataclass
class ObjectData:
	TextureEntry: "Variable 2"

@dataclass
class VisualParam:
	ParamValue: "U8"

@dataclass
class AppearanceData:
	AppearanceVersion: "U8"
	CofVersion: "S32"
	Flags: "U32"

@dataclass
class AppearanceHover:
	HoverHeight: "LLVector3"

@dataclass
class AttachmentBlock:
	ID: "LLUUID"
	AttachmentPoint: "U8"


class AvatarAppearance(Message):

	absolute_id = 4294901918 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Sender = Sender(*((None,)*2))
		self.ObjectData = ObjectData(*((None,)*1))
		self.VisualParam = [VisualParam(*((None,)*1))]
		self.AppearanceData = [AppearanceData(*((None,)*3))]
		self.AppearanceHover = [AppearanceHover(*((None,)*1))]
		self.AttachmentBlock = [AttachmentBlock(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
		self.Sender = Sender(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
		self.ObjectData = ObjectData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.VisualParam = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
			self.VisualParam.append(VisualParam(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AppearanceData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","signed int32","unsigned int32",],remaining_bytes)
			self.AppearanceData.append(AppearanceData(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AppearanceHover = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["vector3",],remaining_bytes)
			self.AppearanceHover.append(AppearanceHover(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AttachmentBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
			self.AttachmentBlock.append(AttachmentBlock(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarAppearance, 
Message Absolute ID: 4294901918
Blocks:
{self.Sender}
{self.ObjectData}
{self.VisualParam}
{self.AppearanceData}
{self.AppearanceHover}
{self.AttachmentBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte",],self.Sender.ID,self.Sender.IsTrial)

		output = output + BytesUtils.pack_bytes_little_endian(["variable2",],self.ObjectData.TextureEntry)

		blocks_count = len(self.VisualParam)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.VisualParam[i].ParamValue)

		blocks_count = len(self.AppearanceData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","signed int32","unsigned int32",],self.AppearanceData[i].AppearanceVersion,self.AppearanceData[i].CofVersion,self.AppearanceData[i].Flags)

		blocks_count = len(self.AppearanceHover)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["vector3",],self.AppearanceHover[i].HoverHeight)

		blocks_count = len(self.AttachmentBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte",],self.AttachmentBlock[i].ID,self.AttachmentBlock[i].AttachmentPoint)

		return output