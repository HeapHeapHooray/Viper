# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass


class SimulatorShutdownRequest(Message):

	absolute_id = 4294901773 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):

		if bytes_data is None:
			return

		remaining_bytes = bytes_data


	def convert_to_string(self) -> str:
		return f"""Message Type: SimulatorShutdownRequest, 
Message Absolute ID: 4294901773
Blocks:"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		return output