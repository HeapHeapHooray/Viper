import UDPSocket
import XMLRPCLogin
import struct
import uuid
import Network
from Messages.UseCircuitCode import UseCircuitCode
from Messages.CompleteAgentMovement import CompleteAgentMovement
from Messages.RegionHandshakeReply import RegionHandshakeReply
from Messages.AgentUpdate import AgentUpdate
import Maths
from getpass import getpass

full_name = input("Enter full name: ")
first_name,last_name = full_name.split(" ")
password = getpass("Enter password: ")

login_result = Network._login("https://login.aditi.lindenlab.com/cgi-bin/login.cgi",first_name,last_name,password,"last")
print(login_result)

code = UseCircuitCode(None)
code.CircuitCode.Code = login_result["circuit_code"]
code.CircuitCode.SessionID = uuid.UUID(login_result["session_id"])
code.CircuitCode.ID = uuid.UUID(login_result["agent_id"])

Network._message_sender.send_message(code)

#data = struct.pack(">BLBL",0x00,0x01,00,0xffff0003) + struct.pack("<L",login_result["circuit_code"]) + uuid.UUID(login_result["session_id"]).bytes + uuid.UUID(login_result["agent_id"]).bytes
#data = struct.pack(">BLBL",0x00,0x01,00,0xffff0003) + code.convert_to_bytes()
#Network._udp_socket.send_data(data)

movement = CompleteAgentMovement(None)
movement.AgentData.AgentID = uuid.UUID(login_result["agent_id"])
movement.AgentData.SessionID = uuid.UUID(login_result["session_id"])
movement.AgentData.CircuitCode = login_result["circuit_code"]

Network._message_sender.send_message(movement)

#data = struct.pack('>BLBL',0x00,0x02,00,0xffff00f9) + uuid.UUID(login_result["agent_id"]).bytes + uuid.UUID(login_result["session_id"]).bytes + struct.pack('<L', login_result["circuit_code"])
#data = struct.pack('>BLBL',0x00,0x02,00,0xffff00f9) + movement.convert_to_bytes()
#Network._udp_socket.send_data(data)

# We send a RegionHandshakeReply cause a RegionHandshake message from sim
# is not needed here.

reply = RegionHandshakeReply(None)
reply.AgentData.AgentID = uuid.UUID(login_result["agent_id"])
reply.AgentData.SessionID = uuid.UUID(login_result["session_id"])
reply.RegionInfo.Flags = 0

Network._message_sender.send_message(reply)

agent_update = AgentUpdate(None)
agent_update.AgentData.AgentID = uuid.UUID(login_result["agent_id"])
agent_update.AgentData.SessionID = uuid.UUID(login_result["session_id"])
agent_update.AgentData.BodyRotation = Maths.Quaternion(0,0,0,1.0)
agent_update.AgentData.HeadRotation = Maths.Quaternion(0,0,0,1.0)
agent_update.AgentData.State = 0
agent_update.AgentData.CameraCenter = Maths.Vec3(161,142,25)
agent_update.AgentData.CameraAtAxis = Maths.Vec3(0,0,0)
agent_update.AgentData.CameraLeftAxis = Maths.Vec3(0,-1.0,0)
agent_update.AgentData.CameraUpAxis = Maths.Vec3(0,0,1.0)
agent_update.AgentData.Far = 128
agent_update.AgentData.ControlFlags = 0
agent_update.AgentData.Flags = 0

Network._message_sender.send_message(agent_update)



#input()
