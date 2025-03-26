# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Data:
	CovenantID: "LLUUID"
	CovenantTimestamp: "U32"
	EstateName: "Variable 1"
	EstateOwnerID: "LLUUID"


class EstateCovenantReply(Message):

	absolute_id = 4294901964 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = Data(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32","variable1","uuid",],remaining_bytes)
		self.Data = Data(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: EstateCovenantReply, 
Message Absolute ID: 4294901964
Blocks:
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32","variable1","uuid",],self.Data.CovenantID,self.Data.CovenantTimestamp,self.Data.EstateName,self.Data.EstateOwnerID)

		return output