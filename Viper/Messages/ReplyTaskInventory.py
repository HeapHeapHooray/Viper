# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class InventoryData:
	TaskID: "LLUUID"
	Serial: "S16"
	Filename: "Variable 1"


class ReplyTaskInventory(Message):

	absolute_id = 4294902050 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.InventoryData = InventoryData(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed int16","variable1",],remaining_bytes)
		self.InventoryData = InventoryData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ReplyTaskInventory, 
Message Absolute ID: 4294902050
Blocks:
{self.InventoryData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed int16","variable1",],self.InventoryData.TaskID,self.InventoryData.Serial,self.InventoryData.Filename)

		return output