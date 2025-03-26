# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class InfoBlock:
	SourceID: "LLUUID"
	DestID: "LLUUID"
	TransactionID: "LLUUID"

@dataclass
class InventoryBlock:
	InventoryID: "LLUUID"
	Type: "S8"

@dataclass
class ValidationBlock:
	NeedsValidation: "BOOL"
	EstateID: "U32"


class TransferInventory(Message):

	absolute_id = 4294902055 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.InfoBlock = InfoBlock(*((None,)*3))
		self.InventoryBlock = [InventoryBlock(*((None,)*2))]
		self.ValidationBlock = ValidationBlock(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","uuid",],remaining_bytes)
		self.InfoBlock = InfoBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.InventoryBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","signed byte",],remaining_bytes)
			self.InventoryBlock.append(InventoryBlock(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned int32",],remaining_bytes)
		self.ValidationBlock = ValidationBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TransferInventory, 
Message Absolute ID: 4294902055
Blocks:
{self.InfoBlock}
{self.InventoryBlock}
{self.ValidationBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","uuid",],self.InfoBlock.SourceID,self.InfoBlock.DestID,self.InfoBlock.TransactionID)

		blocks_count = len(self.InventoryBlock)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid","signed byte",],self.InventoryBlock[i].InventoryID,self.InventoryBlock[i].Type)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned int32",],self.ValidationBlock.NeedsValidation,self.ValidationBlock.EstateID)

		return output