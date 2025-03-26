# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class UserData:
	AgentID: "LLUUID"
	ViewerIP: "IPADDR"
	Disconnect: "BOOL"
	SessionID: "LLUUID"


class DataServerLogout(Message):

	absolute_id = 4294902011 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.UserData = UserData(*((None,)*4))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32","unsigned byte","uuid",],remaining_bytes)
		self.UserData = UserData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: DataServerLogout, 
Message Absolute ID: 4294902011
Blocks:
{self.UserData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32","unsigned byte","uuid",],self.UserData.AgentID,self.UserData.ViewerIP,self.UserData.Disconnect,self.UserData.SessionID)

		return output