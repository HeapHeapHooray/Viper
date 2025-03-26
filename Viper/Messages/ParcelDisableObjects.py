# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class ParcelData:
	LocalID: "S32"
	ReturnType: "U32"

@dataclass
class TaskIDs:
	TaskID: "LLUUID"

@dataclass
class OwnerIDs:
	OwnerID: "LLUUID"


class ParcelDisableObjects(Message):

	absolute_id = 4294901961 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.ParcelData = ParcelData(*((None,)*2))
		self.TaskIDs = [TaskIDs(*((None,)*1))]
		self.OwnerIDs = [OwnerIDs(*((None,)*1))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","unsigned int32",],remaining_bytes)
		self.ParcelData = ParcelData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.TaskIDs = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.TaskIDs.append(TaskIDs(*unpacked_data))

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.OwnerIDs = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
			self.OwnerIDs.append(OwnerIDs(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelDisableObjects, 
Message Absolute ID: 4294901961
Blocks:
{self.AgentData}
{self.ParcelData}
{self.TaskIDs}
{self.OwnerIDs}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","unsigned int32",],self.ParcelData.LocalID,self.ParcelData.ReturnType)

		blocks_count = len(self.TaskIDs)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.TaskIDs[i].TaskID)

		blocks_count = len(self.OwnerIDs)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.OwnerIDs[i].OwnerID)

		return output