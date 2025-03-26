# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AutosaveData:
	PID: "S32"
	Status: "S32"


class ReportAutosaveCrash(Message):

	absolute_id = 4294901888 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AutosaveData = AutosaveData(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","signed int32",],remaining_bytes)
		self.AutosaveData = AutosaveData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ReportAutosaveCrash, 
Message Absolute ID: 4294901888
Blocks:
{self.AutosaveData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","signed int32",],self.AutosaveData.PID,self.AutosaveData.Status)

		return output