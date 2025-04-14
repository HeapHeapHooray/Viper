# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class Sender:
	ID: "LLUUID"
	IsTrial: "BOOL"
SENDER = Sender

@dataclass
class ObjectData:
	TextureEntry: "Variable 2"
OBJECTDATA = ObjectData

@dataclass
class VisualParam:
	ParamValue: "U8"
VISUALPARAM = VisualParam

@dataclass
class AppearanceData:
	AppearanceVersion: "U8"
	CofVersion: "S32"
	Flags: "U32"
APPEARANCEDATA = AppearanceData

@dataclass
class AppearanceHover:
	HoverHeight: "LLVector3"
APPEARANCEHOVER = AppearanceHover

@dataclass
class AttachmentBlock:
	ID: "LLUUID"
	AttachmentPoint: "U8"
ATTACHMENTBLOCK = AttachmentBlock


class AvatarAppearance(Message):

	absolute_id = 4294901918 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.Sender = SENDER(*((None,)*2))

		self.ObjectData = OBJECTDATA(*((None,)*1))

		self.VisualParam = [VISUALPARAM(*((None,)*1))]

		self.AppearanceData = [APPEARANCEDATA(*((None,)*3))]

		self.AppearanceHover = [APPEARANCEHOVER(*((None,)*1))]

		self.AttachmentBlock = [ATTACHMENTBLOCK(*((None,)*2))]

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
		self.Sender = SENDER(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable2",],remaining_bytes)
		self.ObjectData = OBJECTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.VisualParam = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
			self.VisualParam.append(VISUALPARAM(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AppearanceData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","signed int32","unsigned int32",],remaining_bytes)
			self.AppearanceData.append(APPEARANCEDATA(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AppearanceHover = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["vector3",],remaining_bytes)
			self.AppearanceHover.append(APPEARANCEHOVER(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.AttachmentBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
			self.AttachmentBlock.append(ATTACHMENTBLOCK(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarAppearance, Message Absolute ID: 4294901918, Blocks: {self.Sender},{self.ObjectData},{self.VisualParam},{self.AppearanceData},{self.AppearanceHover},{self.AttachmentBlock}"""

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