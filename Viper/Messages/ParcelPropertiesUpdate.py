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
	Flags: "U32"
	ParcelFlags: "U32"
	SalePrice: "S32"
	Name: "Variable 1"
	Desc: "Variable 1"
	MusicURL: "Variable 1"
	MediaURL: "Variable 1"
	MediaID: "LLUUID"
	MediaAutoScale: "U8"
	GroupID: "LLUUID"
	PassPrice: "S32"
	PassHours: "F32"
	Category: "U8"
	AuthBuyerID: "LLUUID"
	SnapshotID: "LLUUID"
	UserLocation: "LLVector3"
	UserLookAt: "LLVector3"
	LandingType: "U8"


class ParcelPropertiesUpdate(Message):

	absolute_id = 4294901958 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.ParcelData = ParcelData(*((None,)*19))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","unsigned int32","unsigned int32","signed int32","variable1","variable1","variable1","variable1","uuid","unsigned byte","uuid","signed int32","float","unsigned byte","uuid","uuid","vector3","vector3","unsigned byte",],remaining_bytes)
		self.ParcelData = ParcelData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelPropertiesUpdate, 
Message Absolute ID: 4294901958
Blocks:
{self.AgentData}
{self.ParcelData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","unsigned int32","unsigned int32","signed int32","variable1","variable1","variable1","variable1","uuid","unsigned byte","uuid","signed int32","float","unsigned byte","uuid","uuid","vector3","vector3","unsigned byte",],self.ParcelData.LocalID,self.ParcelData.Flags,self.ParcelData.ParcelFlags,self.ParcelData.SalePrice,self.ParcelData.Name,self.ParcelData.Desc,self.ParcelData.MusicURL,self.ParcelData.MediaURL,self.ParcelData.MediaID,self.ParcelData.MediaAutoScale,self.ParcelData.GroupID,self.ParcelData.PassPrice,self.ParcelData.PassHours,self.ParcelData.Category,self.ParcelData.AuthBuyerID,self.ParcelData.SnapshotID,self.ParcelData.UserLocation,self.ParcelData.UserLookAt,self.ParcelData.LandingType)

		return output