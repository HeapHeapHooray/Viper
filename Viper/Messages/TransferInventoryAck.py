# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class InfoBlock:
	TransactionID: "LLUUID"
	InventoryID: "LLUUID"
INFOBLOCK = InfoBlock


class TransferInventoryAck(Message):

	absolute_id = 4294902056 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.InfoBlock = INFOBLOCK(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.InfoBlock = INFOBLOCK(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: TransferInventoryAck, Message Absolute ID: 4294902056, Blocks: {self.InfoBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.InfoBlock.TransactionID,self.InfoBlock.InventoryID)

		return output