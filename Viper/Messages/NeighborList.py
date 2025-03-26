# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper

from Message.Message import Message
import BytesUtils
from dataclasses import dataclass

@dataclass
class NeighborBlock:
	IP: "IPADDR"
	Port: "IPPORT"
	PublicIP: "IPADDR"
	PublicPort: "IPPORT"
	RegionID: "LLUUID"
	Name: "Variable 1"
	SimAccess: "U8"


class NeighborList(Message):

	absolute_id = 3 # -- The Full ID of the message

	def __init__(self,bytes_data: bytes):
		self.NeighborBlock = []
		for i in range(4):
			self.NeighborBlock.append(NeighborBlock(*((None,)*7)))

		if bytes_data is None:
			return

		remaining_bytes = bytes_data

		blocks_count = 4 # -- Fixed/constant Blocks length of 4. 

		self.NeighborBlock = []

		for i in range(blocks_count):
			unpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned int16","unsigned int32","unsigned int16","uuid","variable1","unsigned byte",],remaining_bytes)
			self.NeighborBlock.append(NeighborBlock(*unpacked_data))


	def convert_to_string(self) -> str:
		return f"""Message Type: NeighborList, 
Message Absolute ID: 3
Blocks:
{self.NeighborBlock}"""

	def convert_to_bytes(self) -> bytes:
		output = b""

		blocks_count = 4

		for i in range(blocks_count):
			output = output + BytesUtils.pack_bytes_little_endian(["unsigned int32","unsigned int16","unsigned int32","unsigned int16","uuid","variable1","unsigned byte",],self.NeighborBlock[i].IP,self.NeighborBlock[i].Port,self.NeighborBlock[i].PublicIP,self.NeighborBlock[i].PublicPort,self.NeighborBlock[i].RegionID,self.NeighborBlock[i].Name,self.NeighborBlock[i].SimAccess)

		return output