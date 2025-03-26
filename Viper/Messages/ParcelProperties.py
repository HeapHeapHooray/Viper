# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ParcelData:
	RequestResult: "S32"
	SequenceID: "S32"
	SnapSelection: "BOOL"
	SelfCount: "S32"
	OtherCount: "S32"
	PublicCount: "S32"
	LocalID: "S32"
	OwnerID: "LLUUID"
	IsGroupOwned: "BOOL"
	AuctionID: "U32"
	ClaimDate: "S32"
	ClaimPrice: "S32"
	RentPrice: "S32"
	AABBMin: "LLVector3"
	AABBMax: "LLVector3"
	Bitmap: "Variable 2"
	Area: "S32"
	Status: "U8"
	SimWideMaxPrims: "S32"
	SimWideTotalPrims: "S32"
	MaxPrims: "S32"
	TotalPrims: "S32"
	OwnerPrims: "S32"
	GroupPrims: "S32"
	OtherPrims: "S32"
	SelectedPrims: "S32"
	ParcelPrimBonus: "F32"
	OtherCleanTime: "S32"
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
	RegionPushOverride: "BOOL"
	RegionDenyAnonymous: "BOOL"
	RegionDenyIdentified: "BOOL"
	RegionDenyTransacted: "BOOL"

@dataclass
class AgeVerificationBlock:
	RegionDenyAgeUnverified: "BOOL"

@dataclass
class RegionAllowAccessBlock:
	RegionAllowAccessOverride: "BOOL"

@dataclass
class ParcelEnvironmentBlock:
	ParcelEnvironmentVersion: "S32"
	RegionAllowEnvironmentOverride: "BOOL"


class ParcelProperties(Message):

	absolute_id = 23 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ParcelData = ParcelData(*((None,)*49))
		self.AgeVerificationBlock = AgeVerificationBlock(*((None,)*1))
		self.RegionAllowAccessBlock = RegionAllowAccessBlock(*((None,)*1))
		self.ParcelEnvironmentBlock = ParcelEnvironmentBlock(*((None,)*2))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","signed int32","unsigned byte","signed int32","signed int32","signed int32","signed int32","uuid","unsigned byte","unsigned int32","signed int32","signed int32","signed int32","vector3","vector3","variable2","signed int32","unsigned byte","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","float","signed int32","unsigned int32","signed int32","variable1","variable1","variable1","variable1","uuid","unsigned byte","uuid","signed int32","float","unsigned byte","uuid","uuid","vector3","vector3","unsigned byte","unsigned byte","unsigned byte","unsigned byte","unsigned byte",],remaining_bytes)
		self.ParcelData = ParcelData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
		self.AgeVerificationBlock = AgeVerificationBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte",],remaining_bytes)
		self.RegionAllowAccessBlock = RegionAllowAccessBlock(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","unsigned byte",],remaining_bytes)
		self.ParcelEnvironmentBlock = ParcelEnvironmentBlock(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: ParcelProperties, 
Message Absolute ID: 23
Blocks:
{self.ParcelData}
{self.AgeVerificationBlock}
{self.RegionAllowAccessBlock}
{self.ParcelEnvironmentBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","signed int32","unsigned byte","signed int32","signed int32","signed int32","signed int32","uuid","unsigned byte","unsigned int32","signed int32","signed int32","signed int32","vector3","vector3","variable2","signed int32","unsigned byte","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","float","signed int32","unsigned int32","signed int32","variable1","variable1","variable1","variable1","uuid","unsigned byte","uuid","signed int32","float","unsigned byte","uuid","uuid","vector3","vector3","unsigned byte","unsigned byte","unsigned byte","unsigned byte","unsigned byte",],self.ParcelData.RequestResult,self.ParcelData.SequenceID,self.ParcelData.SnapSelection,self.ParcelData.SelfCount,self.ParcelData.OtherCount,self.ParcelData.PublicCount,self.ParcelData.LocalID,self.ParcelData.OwnerID,self.ParcelData.IsGroupOwned,self.ParcelData.AuctionID,self.ParcelData.ClaimDate,self.ParcelData.ClaimPrice,self.ParcelData.RentPrice,self.ParcelData.AABBMin,self.ParcelData.AABBMax,self.ParcelData.Bitmap,self.ParcelData.Area,self.ParcelData.Status,self.ParcelData.SimWideMaxPrims,self.ParcelData.SimWideTotalPrims,self.ParcelData.MaxPrims,self.ParcelData.TotalPrims,self.ParcelData.OwnerPrims,self.ParcelData.GroupPrims,self.ParcelData.OtherPrims,self.ParcelData.SelectedPrims,self.ParcelData.ParcelPrimBonus,self.ParcelData.OtherCleanTime,self.ParcelData.ParcelFlags,self.ParcelData.SalePrice,self.ParcelData.Name,self.ParcelData.Desc,self.ParcelData.MusicURL,self.ParcelData.MediaURL,self.ParcelData.MediaID,self.ParcelData.MediaAutoScale,self.ParcelData.GroupID,self.ParcelData.PassPrice,self.ParcelData.PassHours,self.ParcelData.Category,self.ParcelData.AuthBuyerID,self.ParcelData.SnapshotID,self.ParcelData.UserLocation,self.ParcelData.UserLookAt,self.ParcelData.LandingType,self.ParcelData.RegionPushOverride,self.ParcelData.RegionDenyAnonymous,self.ParcelData.RegionDenyIdentified,self.ParcelData.RegionDenyTransacted)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.AgeVerificationBlock.RegionDenyAgeUnverified)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte",],self.RegionAllowAccessBlock.RegionAllowAccessOverride)

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","unsigned byte",],self.ParcelEnvironmentBlock.ParcelEnvironmentVersion,self.ParcelEnvironmentBlock.RegionAllowEnvironmentOverride)

		return output