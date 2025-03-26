# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class InfoBlock:
	TransactionID: "LLUUID"
	InventoryID: "LLUUID"


class TransferInventoryAck(Message):

	absolute_id = 4294902056 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.InfoBlock = InfoBlock(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.InfoBlock = InfoBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TransferInventoryAck, 
Message Absolute ID: 4294902056
Blocks:
{self.InfoBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.InfoBlock.TransactionID,self.InfoBlock.InventoryID)

		return output