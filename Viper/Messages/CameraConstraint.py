# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class CameraCollidePlane:
	Plane: "LLVector4"


class CameraConstraint(Message):

	absolute_id = 22 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.CameraCollidePlane = CameraCollidePlane(*((None,)*1))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["vector4",],remaining_bytes)
		self.CameraCollidePlane = CameraCollidePlane(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: CameraConstraint, 
Message Absolute ID: 22
Blocks:
{self.CameraCollidePlane}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["vector4",],self.CameraCollidePlane.Plane)

		return output