import hashlib
import xmlrpc.client
import ssl
from typing import List

def login_to_simulator(simulator_login_url: str,first_name: str,last_name: str,password: str,start_location: str,options: List[str]) -> dict:
    md5 = hashlib.md5()
    md5.update(password.encode("utf-8"))
    password_md5 = '$1$' + md5.hexdigest()
    login_details = {
    'first': first_name,
    'last': last_name,
    'passwd': password_md5,
    'start': start_location,
    'major': '1',
    'minor': '18',
    'patch': '5',
    'build': '3',
    'platform': 'Win',
    'mac': "",
    'options': options,
    'user-agent': 'sl.py 0.1',
    'id0': '',
    'agree_to_tos': '',
    'viewer_digest': '09d93740-8f37-c418-fbf2-2a78c7b0d1ea'}
    proxy = xmlrpc.client.ServerProxy(simulator_login_url,context=ssl._create_unverified_context())
    return proxy.login_to_simulator(login_details)
