# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class TaskData:
	TaskID: "LLUUID"
	AttachmentNeedsSave: "BOOL"


class AtomicPassObject(Message):

	absolute_id = 28 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.TaskData = TaskData(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned byte",],remaining_bytes)
		self.TaskData = TaskData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AtomicPassObject, 
Message Absolute ID: 28
Blocks:
{self.TaskData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned byte",],self.TaskData.TaskID,self.TaskData.AttachmentNeedsSave)

		return output