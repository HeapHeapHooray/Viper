from Messages import *

_id_to_class = {}



def get_message_class_from_id(message_id: int):
    return _id_to_class.get(message_id,None)

def _load_message_class(message_class):
    _id_to_class[message_class.absolute_id] = message_class

_load_message_class(StartPingCheck.StartPingCheck)
    
