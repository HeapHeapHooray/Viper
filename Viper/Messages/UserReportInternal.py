# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class ReportData:
	ReportType: "U8"
	Category: "U8"
	ReporterID: "LLUUID"
	ViewerPosition: "LLVector3"
	AgentPosition: "LLVector3"
	ScreenshotID: "LLUUID"
	ObjectID: "LLUUID"
	OwnerID: "LLUUID"
	LastOwnerID: "LLUUID"
	CreatorID: "LLUUID"
	RegionID: "LLUUID"
	AbuserID: "LLUUID"
	AbuseRegionName: "Variable 1"
	AbuseRegionID: "LLUUID"
	Summary: "Variable 1"
	Details: "Variable 2"
	VersionString: "Variable 1"


class UserReportInternal(Message):

	absolute_id = 4294901781 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.ReportData = ReportData(*((None,)*17))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned byte","uuid","vector3","vector3","uuid","uuid","uuid","uuid","uuid","uuid","uuid","variable1","uuid","variable1","variable2","variable1",],remaining_bytes)
		self.ReportData = ReportData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: UserReportInternal, 
Message Absolute ID: 4294901781
Blocks:
{self.ReportData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned byte","uuid","vector3","vector3","uuid","uuid","uuid","uuid","uuid","uuid","uuid","variable1","uuid","variable1","variable2","variable1",],self.ReportData.ReportType,self.ReportData.Category,self.ReportData.ReporterID,self.ReportData.ViewerPosition,self.ReportData.AgentPosition,self.ReportData.ScreenshotID,self.ReportData.ObjectID,self.ReportData.OwnerID,self.ReportData.LastOwnerID,self.ReportData.CreatorID,self.ReportData.RegionID,self.ReportData.AbuserID,self.ReportData.AbuseRegionName,self.ReportData.AbuseRegionID,self.ReportData.Summary,self.ReportData.Details,self.ReportData.VersionString)

		return output