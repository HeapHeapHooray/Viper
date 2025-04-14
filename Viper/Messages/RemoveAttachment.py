# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class AttachmentBlock:
	AttachmentPoint: "U8"
	ItemID: "LLUUID"
ATTACHMENTBLOCK = AttachmentBlock


class RemoveAttachment(Message):

	absolute_id = 4294902092 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*2))
		self.AttachmentBlock = ATTACHMENTBLOCK(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","uuid",],remaining_bytes)
		self.AttachmentBlock = ATTACHMENTBLOCK(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RemoveAttachment, 
Message Absolute ID: 4294902092
Blocks:
{self.AgentData}
{self.AttachmentBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","uuid",],self.AttachmentBlock.AttachmentPoint,self.AttachmentBlock.ItemID)

		return output