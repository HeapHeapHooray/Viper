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
class Data:
	PickID: "LLUUID"
	CreatorID: "LLUUID"
	TopPick: "BOOL"
	ParcelID: "LLUUID"
	Name: "Variable 1"
	Desc: "Variable 2"
	SnapshotID: "LLUUID"
	PosGlobal: "LLVector3d"
	SortOrder: "S32"
	Enabled: "BOOL"
DATA = Data


class PickInfoUpdate(Message):

	absolute_id = 4294901945 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AGENTDATA(*((None,)*2))
		self.Data = DATA(*((None,)*10))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AGENTDATA(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unsigned byte","uuid","variable1","variable2","uuid","vector3d","signed int32","unsigned byte",],remaining_bytes)
		self.Data = DATA(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: PickInfoUpdate, 
Message Absolute ID: 4294901945
Blocks:
{self.AgentData}
{self.Data}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid","unsigned byte","uuid","variable1","variable2","uuid","vector3d","signed int32","unsigned byte",],self.Data.PickID,self.Data.CreatorID,self.Data.TopPick,self.Data.ParcelID,self.Data.Name,self.Data.Desc,self.Data.SnapshotID,self.Data.PosGlobal,self.Data.SortOrder,self.Data.Enabled)

		return output