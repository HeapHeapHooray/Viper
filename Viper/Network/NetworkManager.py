import XMLRPCLogin
from .SimulatorConnectionHandler import SimulatorConnectionHandler
from .IncomingDataRuntime import IncomingDataRuntime
from Events import EventHub
from Message import Message
from Messages.CompletePingCheck import CompletePingCheck

class LoginFailed(Exception):
    pass

class NetworkManager:
    def on_receive_StartPingCheck(self,message: Message):
        complete_ping_check = CompletePingCheck(None)
        if self.last_ping > 255:
            self.last_ping = 0
        complete_ping_check.PingID.PingID = self.last_ping
        self.last_ping = self.last_ping + 1

        self._primary_simulator_connection_handler.send_message(complete_ping_check)

        print("Sent ping check !")
        
    
    def _login(self,simulator_login_url: str,first_name: str,last_name: str,password: str,start_location: str):    
        login_result = XMLRPCLogin.login_to_simulator(simulator_login_url,first_name,last_name,password,start_location,[])

        if login_result["login"] == "false":
            if "message" in login_result:
                raise LoginFailed(login_result["message"])
            raise LoginFailed()

        self._event_hub = EventHub()

        self._event_hub.incoming_messages_event_handler.register_callback("StartPingCheck",self.on_receive_StartPingCheck)
                                                                          
        self._primary_simulator_connection_handler = SimulatorConnectionHandler(login_result["sim_ip"],login_result["sim_port"])
        self._primary_incoming_data_runtime = IncomingDataRuntime(self._primary_simulator_connection_handler,self._event_hub)

        self._primary_incoming_data_runtime.start()

        self.last_ping = 0
        
        return login_result
    
