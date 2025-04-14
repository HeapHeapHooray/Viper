# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
import Utils
from dataclasses import dataclass

@dataclass
class Info:
	AgentID: "LLUUID"
	KickedFromEstateID: "U32"
INFO = Info

@dataclass
class AgentInfo:
	AgentEffectiveMaturity: "U32"
AGENTINFO = AgentInfo


class DataHomeLocationRequest(Message):

	absolute_id = 4294901827 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		self.Info = INFO(*((None,)*2))

		self.AgentInfo = AGENTINFO(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = Utils.zero_decode(bytes_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32",],remaining_bytes)
		self.Info = INFO(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32",],remaining_bytes)
		self.AgentInfo = AGENTINFO(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: DataHomeLocationRequest, Message Absolute ID: 4294901827, Blocks: {self.Info},{self.AgentInfo}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32",],self.Info.AgentID,self.Info.KickedFromEstateID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32",],self.AgentInfo.AgentEffectiveMaturity)

		return output