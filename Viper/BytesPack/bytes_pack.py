# This code can be found at: https://github.com/HeapHeapHooray/BytesPack

import struct
from typing import List
import uuid
import collections

_unsigned_byte_list = ["unsigned byte"]
_signed_byte_list = ["signed byte"]
_unsigned_int16_list = ["unsigned int16"]
_signed_int16_list = ["signed int16"]
_unsigned_int32_list = ["unsigned int32"]
_signed_int32_list = ["signed int32"]
_unsigned_int64_list = ["unsigned int64"]
_signed_int64_list = ["signed int64"]
_float_list = ["float"]
_double_list = ["double"]
_string_list = ["string"]
_uuid_list = ["uuid"]

_smallest_unsigned_int_list = ["smallest unsigned int"]
_smallest_signed_int_list = ["smallest signed int"]

class FoundEndOfDataUnpackingString(Exception):
    pass

def _unpack_unsigned_byte_le(data: bytes):
    unpacked = struct.unpack("<B",bytes([data[0]]))
    return (unpacked[0],data[1::])
def _unpack_signed_byte_le(data: bytes):
    unpacked = struct.unpack("<b",bytes([data[0]]))
    return (unpacked[0],data[1::])
def _unpack_unsigned_int16_le(data: bytes):
    unpacked = struct.unpack("<H",data[0:2])
    return (unpacked[0],data[2::])
def _unpack_signed_int16_le(data: bytes):
    unpacked = struct.unpack("<h",data[0:2])
    return (unpacked[0],data[2::])
def _unpack_unsigned_int32_le(data: bytes):
    unpacked = struct.unpack("<I",data[0:4])
    return (unpacked[0],data[4::])
def _unpack_signed_int32_le(data: bytes):
    unpacked = struct.unpack("<i",data[0:4])
    return (unpacked[0],data[4::])
def _unpack_unsigned_int64_le(data: bytes):
    unpacked = struct.unpack("<Q",data[0:8])
    return (unpacked[0],data[8::])
def _unpack_signed_int64_le(data: bytes):
    unpacked = struct.unpack("<q",data[0:8])
    return (unpacked[0],data[8::])

def _unpack_float_le(data: bytes):
    unpacked = struct.unpack("<f",data[0:4])
    return (unpacked[0],data[4::])
def _unpack_double_le(data: bytes):
    unpacked = struct.unpack("<d",data[0:8])
    return (unpacked[0],data[8::])

def _unpack_unsigned_byte_be(data: bytes):
    unpacked = struct.unpack(">B",bytes([data[0]]))
    return (unpacked[0],data[1::])
def _unpack_signed_byte_be(data: bytes):
    unpacked = struct.unpack(">b",bytes([data[0]]))
    return (unpacked[0],data[1::])
def _unpack_unsigned_int16_be(data: bytes):
    unpacked = struct.unpack(">H",data[0:2])
    return (unpacked[0],data[2::])
def _unpack_signed_int16_be(data: bytes):
    unpacked = struct.unpack(">h",data[0:2])
    return (unpacked[0],data[2::])
def _unpack_unsigned_int32_be(data: bytes):
    unpacked = struct.unpack(">I",data[0:4])
    return (unpacked[0],data[4::])
def _unpack_signed_int32_be(data: bytes):
    unpacked = struct.unpack(">i",data[0:4])
    return (unpacked[0],data[4::])
def _unpack_unsigned_int64_be(data: bytes):
    unpacked = struct.unpack(">Q",data[0:8])
    return (unpacked[0],data[8::])
def _unpack_signed_int64_be(data: bytes):
    unpacked = struct.unpack(">q",data[0:8])
    return (unpacked[0],data[8::])

def _unpack_float_be(data: bytes):
    unpacked = struct.unpack(">f",data[0:4])
    return (unpacked[0],data[4::])
def _unpack_double_be(data: bytes):
    unpacked = struct.unpack(">d",data[0:8])
    return (unpacked[0],data[8::])

def _unpack_string(data: bytes):
    end_index = data.find(0)
    if end_index == -1:
        raise FoundEndOfDataUnpackingString("Found end of data while unpacking a string")
    unpacked = data[0:end_index].decode("utf-8")
    return (unpacked,data[end_index+1::])
def _unpack_uuid(data: bytes):
    return (uuid.UUID(bytes=data[0:16]),data[16::])

def _pack_unsigned_byte_le(byte: int):
    return struct.pack("<B",byte)
def _pack_signed_byte_le(byte: int):
    return struct.pack("<b",byte)
def _pack_unsigned_int16_le(int16: int):
    return struct.pack("<H",int16)
def _pack_signed_int16_le(int16: int):
    return struct.pack("<h",int16)
def _pack_unsigned_int32_le(int32: int):
    return struct.pack("<I",int32)
def _pack_signed_int32_le(int32: int):
    return struct.pack("<i",int32)
def _pack_unsigned_int64_le(int64: int):
    return struct.pack("<Q",int64)
def _pack_signed_int64_le(int64: int):
    return struct.pack("<q",int64)
def _pack_float_le(float: float):
    return struct.pack("<f",float)
def _pack_double_le(double: float):
    return struct.pack("<d",double)

def _pack_smallest_unsigned_int_le(integer: int):
    try:
        return _pack_unsigned_byte_le(integer)
    except struct.error:
        pass
    try:
        return _pack_unsigned_int16_le(integer)
    except struct.error:
        pass
    try:
        return _pack_unsigned_int32_le(integer)
    except struct.error:
        pass
    return _pack_unsigned_int64_le(integer)

def _pack_smallest_signed_int_le(integer: int):
    try:
        return _pack_signed_byte_le(integer)
    except struct.error:
        pass
    try:
        return _pack_signed_int16_le(integer)
    except struct.error:
        pass
    try:
        return _pack_signed_int32_le(integer)
    except struct.error:
        pass
    return _pack_signed_int64_le(integer)

def _pack_unsigned_byte_be(byte: int):
    return struct.pack(">B",byte)
def _pack_signed_byte_be(byte: int):
    return struct.pack(">b",byte)
def _pack_unsigned_int16_be(int16: int):
    return struct.pack(">H",int16)
def _pack_signed_int16_be(int16: int):
    return struct.pack(">h",int16)
def _pack_unsigned_int32_be(int32: int):
    return struct.pack(">I",int32)
def _pack_signed_int32_be(int32: int):
    return struct.pack(">i",int32)
def _pack_unsigned_int64_be(int64: int):
    return struct.pack(">Q",int64)
def _pack_signed_int64_be(int64: int):
    return struct.pack(">q",int64)
def _pack_float_be(float: float):
    return struct.pack(">f",float)
def _pack_double_be(double: float):
    return struct.pack(">d",double)

def _pack_smallest_unsigned_int_be(integer: int):
    try:
        return _pack_unsigned_byte_be(integer)
    except struct.error:
        pass
    try:
        return _pack_unsigned_int16_be(integer)
    except struct.error:
        pass
    try:
        return _pack_unsigned_int32_be(integer)
    except struct.error:
        pass
    return _pack_unsigned_int64_be(integer)

def _pack_smallest_signed_int_be(integer: int):
    try:
        return _pack_signed_byte_be(integer)
    except struct.error:
        pass
    try:
        return _pack_signed_int16_be(integer)
    except struct.error:
        pass
    try:
        return _pack_signed_int32_be(integer)
    except struct.error:
        pass
    return _pack_signed_int64_be(integer)

def _pack_string(string: str):
    return string.encode("utf-8") + bytes([0x00])
def _pack_uuid(uuid: uuid.UUID):
    return uuid.bytes

_unpack_function_dict_le = {}

for element in _unsigned_byte_list:
    _unpack_function_dict_le[element] = _unpack_unsigned_byte_le
for element in _signed_byte_list:
    _unpack_function_dict_le[element] = _unpack_signed_byte_le
for element in _unsigned_int16_list:
    _unpack_function_dict_le[element] = _unpack_unsigned_int16_le
for element in _signed_int16_list:
    _unpack_function_dict_le[element] = _unpack_signed_int16_le
for element in _unsigned_int32_list:
    _unpack_function_dict_le[element] = _unpack_unsigned_int32_le
for element in _signed_int32_list:
    _unpack_function_dict_le[element] = _unpack_signed_int32_le
for element in _unsigned_int64_list:
    _unpack_function_dict_le[element] = _unpack_unsigned_int64_le
for element in _signed_int64_list:
    _unpack_function_dict_le[element] = _unpack_signed_int64_le
for element in _float_list:
    _unpack_function_dict_le[element] = _unpack_float_le
for element in _double_list:
    _unpack_function_dict_le[element] = _unpack_double_le
for element in _string_list:
    _unpack_function_dict_le[element] = _unpack_string
for element in _uuid_list:
    _unpack_function_dict_le[element] = _unpack_uuid

_unpack_function_dict_be = {}

for element in _unsigned_byte_list:
    _unpack_function_dict_be[element] = _unpack_unsigned_byte_be
for element in _signed_byte_list:
    _unpack_function_dict_be[element] = _unpack_signed_byte_be
for element in _unsigned_int16_list:
    _unpack_function_dict_be[element] = _unpack_unsigned_int16_be
for element in _signed_int16_list:
    _unpack_function_dict_be[element] = _unpack_signed_int16_be
for element in _unsigned_int32_list:
    _unpack_function_dict_be[element] = _unpack_unsigned_int32_be
for element in _signed_int32_list:
    _unpack_function_dict_be[element] = _unpack_signed_int32_be
for element in _unsigned_int64_list:
    _unpack_function_dict_be[element] = _unpack_unsigned_int64_be
for element in _signed_int64_list:
    _unpack_function_dict_be[element] = _unpack_signed_int64_be
for element in _float_list:
    _unpack_function_dict_be[element] = _unpack_float_be
for element in _double_list:
    _unpack_function_dict_be[element] = _unpack_double_be
for element in _string_list:
    _unpack_function_dict_be[element] = _unpack_string
for element in _uuid_list:
    _unpack_function_dict_be[element] = _unpack_uuid

_pack_function_dict_le = {}

for element in _unsigned_byte_list:
    _pack_function_dict_le[element] = _pack_unsigned_byte_le
for element in _signed_byte_list:
    _pack_function_dict_le[element] = _pack_signed_byte_le
for element in _unsigned_int16_list:
    _pack_function_dict_le[element] = _pack_unsigned_int16_le
for element in _signed_int16_list:
    _pack_function_dict_le[element] = _pack_signed_int16_le
for element in _unsigned_int32_list:
    _pack_function_dict_le[element] = _pack_unsigned_int32_le
for element in _signed_int32_list:
    _pack_function_dict_le[element] = _pack_signed_int32_le
for element in _unsigned_int64_list:
    _pack_function_dict_le[element] = _pack_unsigned_int64_le
for element in _signed_int64_list:
    _pack_function_dict_le[element] = _pack_signed_int64_le
for element in _float_list:
    _pack_function_dict_le[element] = _pack_float_le
for element in _double_list:
    _pack_function_dict_le[element] = _pack_double_le
for element in _string_list:
    _pack_function_dict_le[element] = _pack_string
for element in _uuid_list:
    _pack_function_dict_le[element] = _pack_uuid
for element in _smallest_unsigned_int_list:
    _pack_function_dict_le[element] = _pack_smallest_unsigned_int_le
for element in _smallest_signed_int_list:
    _pack_function_dict_le[element] = _pack_smallest_signed_int_le

_pack_function_dict_be = {}

for element in _unsigned_byte_list:
    _pack_function_dict_be[element] = _pack_unsigned_byte_be
for element in _signed_byte_list:
    _pack_function_dict_be[element] = _pack_signed_byte_be
for element in _unsigned_int16_list:
    _pack_function_dict_be[element] = _pack_unsigned_int16_be
for element in _signed_int16_list:
    _pack_function_dict_be[element] = _pack_signed_int16_be
for element in _unsigned_int32_list:
    _pack_function_dict_be[element] = _pack_unsigned_int32_be
for element in _signed_int32_list:
    _pack_function_dict_be[element] = _pack_signed_int32_be
for element in _unsigned_int64_list:
    _pack_function_dict_be[element] = _pack_unsigned_int64_be
for element in _signed_int64_list:
    _pack_function_dict_be[element] = _pack_signed_int64_be
for element in _float_list:
    _pack_function_dict_be[element] = _pack_float_be
for element in _double_list:
    _pack_function_dict_be[element] = _pack_double_be
for element in _string_list:
    _pack_function_dict_be[element] = _pack_string
for element in _uuid_list:
    _pack_function_dict_be[element] = _pack_uuid
for element in _smallest_unsigned_int_list:
    _pack_function_dict_be[element] = _pack_smallest_unsigned_int_be
for element in _smallest_signed_int_list:
    _pack_function_dict_be[element] = _pack_smallest_signed_int_be

_type_minimum_sizes = {}

for element in _unsigned_byte_list:
    _type_minimum_sizes[element] = 1
for element in _signed_byte_list:
    _type_minimum_sizes[element] = 1
for element in _unsigned_int16_list:
    _type_minimum_sizes[element] = 2
for element in _signed_int16_list:
    _type_minimum_sizes[element] = 2
for element in _unsigned_int32_list:
    _type_minimum_sizes[element] = 4
for element in _signed_int32_list:
    _type_minimum_sizes[element] = 4
for element in _unsigned_int64_list:
    _type_minimum_sizes[element] = 8
for element in _signed_int64_list:
    _type_minimum_sizes[element] = 8
for element in _float_list:
    _type_minimum_sizes[element] = 4
for element in _double_list:
    _type_minimum_sizes[element] = 8
for element in _string_list:
    _type_minimum_sizes[element] = 1
for element in _uuid_list:
    _type_minimum_sizes[element] = 16
    
def pack_bytes_little_endian(data_format: List[str],*args):
    packed_bytes = bytearray()

    for i in range(0,len(data_format)):
        packed = _pack_function_dict_le[data_format[i]](args[i])
        packed_bytes += packed

    return bytes(packed_bytes)

def pack_bytes_big_endian(data_format: List[str],*args):
    packed_bytes = bytearray()

    for i in range(0,len(data_format)):
        packed = _pack_function_dict_be[data_format[i]](args[i])
        packed_bytes += packed

    return bytes(packed_bytes)

UnpackResult = collections.namedtuple("UnpackResult",["unpacked_data","remaining_bytes"])

def unpack_bytes_little_endian(data_format: List[str],data: bytes):
    unpacked = []
    current_data = data
    for element in data_format:
        unpacked_element,current_data = _unpack_function_dict_le[element](current_data)
        unpacked.append(unpacked_element)
    return UnpackResult(unpacked,current_data)

def unpack_bytes_big_endian(data_format: List[str],data: bytes):
    unpacked = []
    current_data = data
    for element in data_format:
        unpacked_element,current_data = _unpack_function_dict_be[element](current_data)
        unpacked.append(unpacked_element)
    return UnpackResult(unpacked,current_data)

def calculate_minimum_size(data_format: List[str]):
    return sum(_type_minimum_sizes[element] for element in data_format)

    
