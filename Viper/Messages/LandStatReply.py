# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class RequestData:
	ReportType: "U32"
	RequestFlags: "U32"
	TotalObjectCount: "U32"

@dataclass
class ReportData:
	TaskLocalID: "U32"
	TaskID: "LLUUID"
	LocationX: "F32"
	LocationY: "F32"
	LocationZ: "F32"
	Score: "F32"
	TaskName: "Variable 1"
	OwnerName: "Variable 1"


class LandStatReply(Message):

	absolute_id = 4294902182 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.RequestData = RequestData(*((None,)*3))
		self.ReportData = [ReportData(*((None,)*8))]

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32",],remaining_bytes)
		self.RequestData = RequestData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)
		blocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.

		self.ReportData = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","uuid","float","float","float","float","variable1","variable1",],remaining_bytes)
			self.ReportData.append(ReportData(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: LandStatReply, 
Message Absolute ID: 4294902182
Blocks:
{self.RequestData}
{self.ReportData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int32","unsigned int32",],self.RequestData.ReportType,self.RequestData.RequestFlags,self.RequestData.TotalObjectCount)

		blocks_count = len(self.ReportData)
		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","uuid","float","float","float","float","variable1","variable1",],self.ReportData[i].TaskLocalID,self.ReportData[i].TaskID,self.ReportData[i].LocationX,self.ReportData[i].LocationY,self.ReportData[i].LocationZ,self.ReportData[i].Score,self.ReportData[i].TaskName,self.ReportData[i].OwnerName)

		return output