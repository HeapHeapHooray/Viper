# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Data:
	TaskID: "LLUUID"
	ItemID: "LLUUID"
	ObjectName: "Variable 1"
	ObjectOwner: "Variable 1"
	Questions: "S32"

@dataclass
class Experience:
	ExperienceID: "LLUUID"


class ScriptQuestion(Message):

	absolute_id = 4294901948 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = Data(*((None,)*5))
		self.Experience = Experience(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","variable1","variable1","signed int32",],remaining_bytes)
		self.Data = Data(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.Experience = Experience(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ScriptQuestion, 
Message Absolute ID: 4294901948
Blocks:
{self.Data}
{self.Experience}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","variable1","variable1","signed int32",],self.Data.TaskID,self.Data.ItemID,self.Data.ObjectName,self.Data.ObjectOwner,self.Data.Questions)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.Experience.ExperienceID)

		return output