import UDPSocket
import XMLRPCLogin
import threading
import Packet
from Messages.UnknownMessage import UnknownMessage
from Messages.ImprovedTerseObjectUpdate import ImprovedTerseObjectUpdate
from Messages.StartPingCheck import StartPingCheck
from Messages.CompletePingCheck import CompletePingCheck
import MessageSender

_udp_socket = None
_receiving_data = False
_receive_data_thread = None

_message_sender = None

last_ping = 0

class LoginFailed(Exception):
    pass

def _login(simulator_login_url: str,first_name: str,last_name: str,password: str,start_location: str):    
    login_result = XMLRPCLogin.login_to_simulator(simulator_login_url,first_name,last_name,password,start_location,[])

    if login_result["login"] == "false":
        if "message" in login_result:
            raise LoginFailed(login_result["message"])
        raise LoginFailed()

    global _udp_socket
    global _receiving_data
    global _receive_data_thread
    global _message_sender

    _udp_socket = UDPSocket.UDPSocket(login_result["sim_ip"],login_result["sim_port"],8096)
    _receiving_data = True
    _receive_data_thread = threading.Thread(target=_receive_data)
    _receive_data_thread.start()

    _message_sender = MessageSender.MessageSender(_udp_socket)
    
    return login_result

def _receive_data():
    global _udp_socket
    while _receiving_data:
        data = _udp_socket.receive_data()
        #print(data)
        try:
            packet = Packet.PacketFactory.create_from_bytes(data[0])
            if isinstance(packet.message,UnknownMessage):
                print("Unknown Message's ID:",packet.message.message_id)
            elif isinstance(packet.message,StartPingCheck):
                complete_ping_check = CompletePingCheck(None)
                global last_ping
                if last_ping > 255:
                    last_ping = 0
                complete_ping_check.PingID.PingID = last_ping
                last_ping = last_ping + 1

                _message_sender.send_message(complete_ping_check)

                print("Sent ping check !")
                print(packet.message.convert_to_string())
                
            elif isinstance(packet.message,ImprovedTerseObjectUpdate):
                data = packet.message.ObjectData[0].Data
                import BytesUtils
                udata,remaining = BytesUtils.unpack_bytes_little_endian(["unsigned int32","unsigned byte","unsigned byte"],data)
                avatar = udata[2]
                if avatar:
                    udata,remaining = BytesUtils.unpack_bytes_little_endian(["vector4","vector3"],remaining)
                    position = udata[1]
                else:
                    udata,remaining = BytesUtils.unpack_bytes_little_endian(["vector3"],remaining)
                    position = udata[0]
                print("Avatar:",avatar,"\nPosition:",position.convert_to_string())
                #print(packet.convert_to_string())
        except Exception as e:
            pass#print("Network's data receiving loop raised the following exception:",e)
    
