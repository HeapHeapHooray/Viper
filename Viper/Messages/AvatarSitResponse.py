# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class SitObject:
	ID: "LLUUID"

@dataclass
class SitTransform:
	AutoPilot: "BOOL"
	SitPosition: "LLVector3"
	SitRotation: "LLQuaternion"
	CameraEyeOffset: "LLVector3"
	CameraAtOffset: "LLVector3"
	ForceMouselook: "BOOL"


class AvatarSitResponse(Message):

	absolute_id = 21 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.SitObject = SitObject(*((None,)*1))
		self.SitTransform = SitTransform(*((None,)*6))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.SitObject = SitObject(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","vector3","unit_quaternion","vector3","vector3","unsigned byte",],remaining_bytes)
		self.SitTransform = SitTransform(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: AvatarSitResponse, 
Message Absolute ID: 21
Blocks:
{self.SitObject}
{self.SitTransform}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.SitObject.ID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","vector3","unit_quaternion","vector3","vector3","unsigned byte",],self.SitTransform.AutoPilot,self.SitTransform.SitPosition,self.SitTransform.SitRotation,self.SitTransform.CameraEyeOffset,self.SitTransform.CameraAtOffset,self.SitTransform.ForceMouselook)

		return output