# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Data:
	ObjectName: "Variable 1"
	ObjectID: "LLUUID"
	OwnerID: "LLUUID"
	OwnerIsGroup: "BOOL"
	Message: "Variable 1"
	URL: "Variable 1"


class LoadURL(Message):

	absolute_id = 4294901954 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = Data(*((None,)*6))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["variable1","uuid","uuid","unsigned byte","variable1","variable1",],remaining_bytes)
		self.Data = Data(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: LoadURL, 
Message Absolute ID: 4294901954
Blocks:
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["variable1","uuid","uuid","unsigned byte","variable1","variable1",],self.Data.ObjectName,self.Data.ObjectID,self.Data.OwnerID,self.Data.OwnerIsGroup,self.Data.Message,self.Data.URL)

		return output