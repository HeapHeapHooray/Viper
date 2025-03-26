# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class Data:
	TransactionID: "LLUUID"
	TransactionTime: "U32"
	SourceID: "LLUUID"
	DestID: "LLUUID"
	OwnerID: "LLUUID"
	Flags: "U8"
	TransactionType: "S32"
	Amount: "S32"
	BillableArea: "S32"
	ActualArea: "S32"
	Final: "BOOL"

@dataclass
class RegionData:
	RegionID: "LLUUID"
	GridX: "U32"
	GridY: "U32"


class RequestParcelTransfer(Message):

	absolute_id = 4294901980 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.Data = Data(*((None,)*11))
		self.RegionData = RegionData(*((None,)*3))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32","uuid","uuid","uuid","unsigned byte","signed int32","signed int32","signed int32","signed int32","unsigned byte",],remaining_bytes)
		self.Data = Data(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","unsigned int32","unsigned int32",],remaining_bytes)
		self.RegionData = RegionData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: RequestParcelTransfer, 
Message Absolute ID: 4294901980
Blocks:
{self.Data}
{self.RegionData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32","uuid","uuid","uuid","unsigned byte","signed int32","signed int32","signed int32","signed int32","unsigned byte",],self.Data.TransactionID,self.Data.TransactionTime,self.Data.SourceID,self.Data.DestID,self.Data.OwnerID,self.Data.Flags,self.Data.TransactionType,self.Data.Amount,self.Data.BillableArea,self.Data.ActualArea,self.Data.Final)

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","unsigned int32","unsigned int32",],self.RegionData.RegionID,self.RegionData.GridX,self.RegionData.GridY)

		return output