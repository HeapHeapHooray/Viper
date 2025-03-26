# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Info:
	ObjectCapacity: "S32"
	ObjectCount: "S32"
	PriceEnergyUnit: "S32"
	PriceObjectClaim: "S32"
	PricePublicObjectDecay: "S32"
	PricePublicObjectDelete: "S32"
	PriceParcelClaim: "S32"
	PriceParcelClaimFactor: "F32"
	PriceUpload: "S32"
	PriceRentLight: "S32"
	TeleportMinPrice: "S32"
	TeleportPriceExponent: "F32"
	EnergyEfficiency: "F32"
	PriceObjectRent: "F32"
	PriceObjectScaleFactor: "F32"
	PriceParcelRent: "S32"
	PriceGroupCreate: "S32"


class EconomyData(Message):

	absolute_id = 4294901785 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Info = Info(*((None,)*17))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","float","signed int32","signed int32","signed int32","float","float","float","float","signed int32","signed int32",],remaining_bytes)
		self.Info = Info(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: EconomyData, 
Message Absolute ID: 4294901785
Blocks:
{self.Info}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","signed int32","float","signed int32","signed int32","signed int32","float","float","float","float","signed int32","signed int32",],self.Info.ObjectCapacity,self.Info.ObjectCount,self.Info.PriceEnergyUnit,self.Info.PriceObjectClaim,self.Info.PricePublicObjectDecay,self.Info.PricePublicObjectDelete,self.Info.PriceParcelClaim,self.Info.PriceParcelClaimFactor,self.Info.PriceUpload,self.Info.PriceRentLight,self.Info.TeleportMinPrice,self.Info.TeleportPriceExponent,self.Info.EnergyEfficiency,self.Info.PriceObjectRent,self.Info.PriceObjectScaleFactor,self.Info.PriceParcelRent,self.Info.PriceGroupCreate)

		return output