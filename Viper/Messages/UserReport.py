# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class AgentData:
	AgentID: "LLUUID"
	SessionID: "LLUUID"

@dataclass
class ReportData:
	ReportType: "U8"
	Category: "U8"
	Position: "LLVector3"
	CheckFlags: "U8"
	ScreenshotID: "LLUUID"
	ObjectID: "LLUUID"
	AbuserID: "LLUUID"
	AbuseRegionName: "Variable 1"
	AbuseRegionID: "LLUUID"
	Summary: "Variable 1"
	Details: "Variable 2"
	VersionString: "Variable 1"


class UserReport(Message):

	absolute_id = 4294901893 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.AgentData = AgentData(*((None,)*2))
		self.ReportData = ReportData(*((None,)*12))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["uuid","uuid",],remaining_bytes)
		self.AgentData = AgentData(*unpacked_data)

		unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte","unsigned byte","vector3","unsigned byte","uuid","uuid","uuid","variable1","uuid","variable1","variable2","variable1",],remaining_bytes)
		self.ReportData = ReportData(*unpacked_data)


	def convert_to_string(self) -> str:
		return f"""Message Type: UserReport, 
Message Absolute ID: 4294901893
Blocks:
{self.AgentData}
{self.ReportData}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		output = output + BytesUtils.pack_bytes_little_endian(["uuid","uuid",],self.AgentData.AgentID,self.AgentData.SessionID)

		output = output + BytesUtils.pack_bytes_little_endian(["unsigned byte","unsigned byte","vector3","unsigned byte","uuid","uuid","uuid","variable1","uuid","variable1","variable2","variable1",],self.ReportData.ReportType,self.ReportData.Category,self.ReportData.Position,self.ReportData.CheckFlags,self.ReportData.ScreenshotID,self.ReportData.ObjectID,self.ReportData.AbuserID,self.ReportData.AbuseRegionName,self.ReportData.AbuseRegionID,self.ReportData.Summary,self.ReportData.Details,self.ReportData.VersionString)

		return output