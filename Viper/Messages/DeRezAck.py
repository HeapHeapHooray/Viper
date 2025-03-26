# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TransactionData:
	TransactionID: "LLUUID"
	Success: "BOOL"


class DeRezAck(Message):

	absolute_id = 4294902052 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TransactionData = TransactionData(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
		self.TransactionData = TransactionData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: DeRezAck, 
Message Absolute ID: 4294902052
Blocks:
{self.TransactionData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte",],self.TransactionData.TransactionID,self.TransactionData.Success)

		return output