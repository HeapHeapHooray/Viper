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
code.circuit_code = login_result["circuit_code"]
code.session_uuid = uuid.UUID(login_result["session_id"])
code.agent_uuid = uuid.UUID(login_result["agent_id"])

Network._message_sender.send_message(code)

#data = struct.pack(">BLBL",0x00,0x01,00,0xffff0003) + struct.pack("<L",login_result["circuit_code"]) + uuid.UUID(login_result["session_id"]).bytes + uuid.UUID(login_result["agent_id"]).bytes
#data = struct.pack(">BLBL",0x00,0x01,00,0xffff0003) + code.convert_to_bytes()
#Network._udp_socket.send_data(data)

movement = CompleteAgentMovement(None)
movement.agent_uuid = uuid.UUID(login_result["agent_id"])
movement.session_uuid = uuid.UUID(login_result["session_id"])
movement.circuit_code = login_result["circuit_code"]

Network._message_sender.send_message(movement)

#data = struct.pack('>BLBL',0x00,0x02,00,0xffff00f9) + uuid.UUID(login_result["agent_id"]).bytes + uuid.UUID(login_result["session_id"]).bytes + struct.pack('<L', login_result["circuit_code"])
#data = struct.pack('>BLBL',0x00,0x02,00,0xffff00f9) + movement.convert_to_bytes()
#Network._udp_socket.send_data(data)

# We send a RegionHandshakeReply here cause a RegionHandshake message from sim
# is not needed here.

reply = RegionHandshakeReply(None)
reply.agent_uuid = uuid.UUID(login_result["agent_id"])
reply.session_uuid = uuid.UUID(login_result["session_id"])
reply.region_info_flags = 0

Network._message_sender.send_message(reply)

agent_update = AgentUpdate(None)
agent_update.agent_uuid = uuid.UUID(login_result["agent_id"])
agent_update.session_uuid = uuid.UUID(login_result["session_id"])
agent_update.body_rotation = Maths.Quaternion(0,0,0,1.0)
agent_update.head_rotation = Maths.Quaternion(0,0,0,1.0)
agent_update.state = 0
agent_update.camera_center = Maths.Vec3(0,0,0)
agent_update.camera_at_axis = Maths.Vec3(0,0,0)
agent_update.camera_left_axis = Maths.Vec3(0,0,0)
agent_update.camera_up_axis = Maths.Vec3(0,0,0)
agent_update.far = 128
agent_update.control_flags = 0
agent_update.flags = 0

Network._message_sender.send_message(agent_update)



input()
