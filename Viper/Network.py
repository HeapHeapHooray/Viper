import UDPSocket
import XMLRPCLogin
import threading
import Packet
from Messages.UnknownMessage import UnknownMessage
import MessageSender
import parse_message_template as MessageTemplate

_udp_socket = None
_receiving_data = False
_receive_data_thread = None

_message_sender = None

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
        packet = Packet.PacketFactory.create_from_bytes(data[0])
        messages = MessageTemplate.get_messages_by_absolute_id()
        if isinstance(packet.message,UnknownMessage):
            print(messages[packet.message.message_id].get_message_name())
        else:
            print(packet.convert_to_string())
    
