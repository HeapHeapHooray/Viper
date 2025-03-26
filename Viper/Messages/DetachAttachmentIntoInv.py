# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ObjectData:
	AgentID: "LLUUID"
	ItemID: "LLUUID"


class DetachAttachmentIntoInv(Message):

	absolute_id = 4294902157 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ObjectData = ObjectData(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.ObjectData = ObjectData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: DetachAttachmentIntoInv, 
Message Absolute ID: 4294902157
Blocks:
{self.ObjectData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.ObjectData.AgentID,self.ObjectData.ItemID)

		return output