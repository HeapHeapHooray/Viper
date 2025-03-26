# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class XferID:
	ID: "U64"
	Filename: "Variable 1"
	FilePath: "U8"
	DeleteOnCompletion: "BOOL"
	UseBigPackets: "BOOL"
	VFileID: "LLUUID"
	VFileType: "S16"


class RequestXfer(Message):

	absolute_id = 4294901916 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.XferID = XferID(*((None,)*7))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int64","variable1","unsigned byte","unsigned byte","unsigned byte","uuid","signed int16",],remaining_bytes)
		self.XferID = XferID(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RequestXfer, 
Message Absolute ID: 4294901916
Blocks:
{self.XferID}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int64","variable1","unsigned byte","unsigned byte","unsigned byte","uuid","signed int16",],self.XferID.ID,self.XferID.Filename,self.XferID.FilePath,self.XferID.DeleteOnCompletion,self.XferID.UseBigPackets,self.XferID.VFileID,self.XferID.VFileType)

		return output