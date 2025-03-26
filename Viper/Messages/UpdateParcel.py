# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ParcelData:
	ParcelID: "LLUUID"
	RegionHandle: "U64"
	OwnerID: "LLUUID"
	GroupOwned: "BOOL"
	Status: "U8"
	Name: "Variable 1"
	Description: "Variable 1"
	MusicURL: "Variable 1"
	RegionX: "F32"
	RegionY: "F32"
	ActualArea: "S32"
	BillableArea: "S32"
	ShowDir: "BOOL"
	IsForSale: "BOOL"
	Category: "U8"
	SnapshotID: "LLUUID"
	UserLocation: "LLVector3"
	SalePrice: "S32"
	AuthorizedBuyerID: "LLUUID"
	AllowPublish: "BOOL"
	MaturePublish: "BOOL"


class UpdateParcel(Message):

	absolute_id = 4294901981 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ParcelData = ParcelData(*((None,)*21))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int64","uuid","unsigned byte","unsigned byte","variable1","variable1","variable1","float","float","signed int32","signed int32","unsigned byte","unsigned byte","unsigned byte","uuid","vector3","signed int32","uuid","unsigned byte","unsigned byte",],remaining_bytes)
		self.ParcelData = ParcelData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: UpdateParcel, 
Message Absolute ID: 4294901981
Blocks:
{self.ParcelData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int64","uuid","unsigned byte","unsigned byte","variable1","variable1","variable1","float","float","signed int32","signed int32","unsigned byte","unsigned byte","unsigned byte","uuid","vector3","signed int32","uuid","unsigned byte","unsigned byte",],self.ParcelData.ParcelID,self.ParcelData.RegionHandle,self.ParcelData.OwnerID,self.ParcelData.GroupOwned,self.ParcelData.Status,self.ParcelData.Name,self.ParcelData.Description,self.ParcelData.MusicURL,self.ParcelData.RegionX,self.ParcelData.RegionY,self.ParcelData.ActualArea,self.ParcelData.BillableArea,self.ParcelData.ShowDir,self.ParcelData.IsForSale,self.ParcelData.Category,self.ParcelData.SnapshotID,self.ParcelData.UserLocation,self.ParcelData.SalePrice,self.ParcelData.AuthorizedBuyerID,self.ParcelData.AllowPublish,self.ParcelData.MaturePublish)

		return output