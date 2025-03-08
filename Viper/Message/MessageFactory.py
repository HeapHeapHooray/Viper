import BytesUtils
from . import MessageDecoder
from Messages.UnknownMessage import UnknownMessage

def _get_message_id_frequency_rate(message_id: bytes) -> str:
    if message_id[0] == int("FF",base=16):
        if message_id[1] == int("FF",base=16):
            if message_id[2] == int("FF",base=16):
                return "Fixed"
            return "Low"
        return "Medium"
    return "High"

def _get_id_data_type(message_id: bytes) -> str:
    frequency = _get_message_id_frequency_rate(message_id)

    if frequency == "High":
        return "unsigned byte"
    if frequency == "Medium":
        return "unsigned int16"
    if frequency == "Low" or frequency == "Fixed":
        return "unsigned int32"

def create_from_bytes(bytes_data: bytes):
    id_data_type = _get_id_data_type(bytes_data)

    unpack_result = BytesUtils.unpack_bytes_big_endian([id_data_type],bytes_data)

    message_id = unpack_result.unpacked_data[0]
    message_blocks_data = unpack_result.remaining_bytes

    message_class = MessageDecoder.get_message_class_from_id(message_id)
    
    if message_class is None:
        message_instance = UnknownMessage(message_id,message_blocks_data)
    else:
        message_instance = message_class(message_blocks_data)

    return message_instance
        

    
