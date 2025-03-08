import UDPSocket
import XMLRPCLogin
import struct
import uuid
import Network
from Messages.UseCircuitCode import UseCircuitCode
from Messages.CompleteAgentMovement import CompleteAgentMovement
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

input()
