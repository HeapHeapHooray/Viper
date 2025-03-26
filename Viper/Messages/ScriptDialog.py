# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Data:
	ObjectID: "LLUUID"
	FirstName: "Variable 1"
	LastName: "Variable 1"
	ObjectName: "Variable 1"
	Message: "Variable 2"
	ChatChannel: "S32"
	ImageID: "LLUUID"

@dataclass
class Buttons:
	ButtonLabel: "Variable 1"

@dataclass
class OwnerData:
	OwnerID: "LLUUID"


class ScriptDialog(Message):

	absolute_id = 4294901950 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = Data(*((None,)*7))
		self.Buttons = [Buttons(*((None,)*1))]
		self.OwnerData = [OwnerData(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","variable1","variable1","variable1","variable2","signed int32","uuid",],remaining_bytes)
		self.Data = Data(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.Buttons = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1",],remaining_bytes)
			self.Buttons.append(Buttons(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.OwnerData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.OwnerData.append(OwnerData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ScriptDialog, 
Message Absolute ID: 4294901950
Blocks:
{self.Data}
{self.Buttons}
{self.OwnerData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","variable1","variable1","variable1","variable2","signed int32","uuid",],self.Data.ObjectID,self.Data.FirstName,self.Data.LastName,self.Data.ObjectName,self.Data.Message,self.Data.ChatChannel,self.Data.ImageID)

		blocks_count = len(self.Buttons)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["variable1",],self.Buttons[i].ButtonLabel)

		blocks_count = len(self.OwnerData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.OwnerData[i].OwnerID)

		return output