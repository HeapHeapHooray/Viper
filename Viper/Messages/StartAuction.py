# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
AGENTDATA = AgentData

@dataclass
class ParcelData:
	ParcelID: "LLUUID"
	SnapshotID: "LLUUID"
	Name: "Variable 1"
PARCELDATA = ParcelData


class StartAuction(Message):

	absolute_id = 4294901989 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*1))
		self.ParcelData = PARCELDATA(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","variable1",],remaining_bytes)
		self.ParcelData = PARCELDATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: StartAuction, 
Message Absolute ID: 4294901989
Blocks:
{self.AgentData}
{self.ParcelData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid",],self.AgentData.AgentID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","variable1",],self.ParcelData.ParcelID,self.ParcelData.SnapshotID,self.ParcelData.Name)

		return output