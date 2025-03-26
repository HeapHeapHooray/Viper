from .BytesPack import BytesPack
from typing import List
import math

pack_bytes_big_endian = BytesPack.pack_bytes_big_endian
pack_bytes_little_endian = BytesPack.pack_bytes_little_endian
unpack_bytes_big_endian = BytesPack.unpack_bytes_big_endian
unpack_bytes_little_endian = BytesPack.unpack_bytes_little_endian
calculate_minimum_size = BytesPack.calculate_minimum_size

BytesPack._type_minimum_sizes["vector3"] = 12
BytesPack._type_minimum_sizes["vec3"] = 12
BytesPack._type_minimum_sizes["vector3d"] = 24
BytesPack._type_minimum_sizes["vec3d"] = 24
BytesPack._type_minimum_sizes["unit_quaternion"] = 12
BytesPack._type_minimum_sizes["variable1"] = 1
BytesPack._type_minimum_sizes["variable2"] = 2
BytesPack._type_minimum_sizes["fixed32"] = 32

def _pack_vector3(vec3):
    return vec3.convert_to_bytes()
def _pack_vector3d(vec3):
    return vec3.convert_as_doubles_to_bytes()
def _pack_unitary_quaternion(quat):
    return quat.convert_to_bytes()
def _pack_variable1(data: bytes):
    return pack_bytes_little_endian(["unsigned byte"],len(data))+data
def _pack_variable2_be(data: bytes):
    return pack_bytes_big_endian(["unsigned int16"],len(data))+data
def _pack_variable2_le(data: bytes):
    return pack_bytes_little_endian(["unsigned int16"],len(data))+data
def _pack_fixed32(data: bytes):
    return data


BytesPack._pack_function_dict_be["vector3"] = _pack_vector3
BytesPack._pack_function_dict_be["vec3"] = _pack_vector3
BytesPack._pack_function_dict_be["vector3d"] = _pack_vector3d
BytesPack._pack_function_dict_be["vec3d"] = _pack_vector3d
BytesPack._pack_function_dict_be["unit_quaternion"] = _pack_unitary_quaternion
BytesPack._pack_function_dict_be["variable1"] = _pack_variable1
BytesPack._pack_function_dict_be["variable2"] = _pack_variable2_be
BytesPack._pack_function_dict_be["fixed32"] = _pack_fixed32
BytesPack._pack_function_dict_le["vector3"] = _pack_vector3
BytesPack._pack_function_dict_le["vec3"] = _pack_vector3
BytesPack._pack_function_dict_le["vector3d"] = _pack_vector3d
BytesPack._pack_function_dict_le["vec3d"] = _pack_vector3d
BytesPack._pack_function_dict_le["unit_quaternion"] = _pack_unitary_quaternion
BytesPack._pack_function_dict_le["variable1"] = _pack_variable1
BytesPack._pack_function_dict_le["variable2"] = _pack_variable2_le
BytesPack._pack_function_dict_le["fixed32"] = _pack_fixed32

def _unpack_vector3(data: bytes):
    import Maths
    unpack_result = BytesPack.unpack_bytes_big_endian(["float","float","float"],data)
    return (Maths.Vec3(*unpack_result.unpacked_data),unpack_result.remaining_bytes)
def _unpack_vector3d(data: bytes):
    import Maths
    unpack_result = BytesPack.unpack_bytes_big_endian(["double","double","double"],data)
    return (Maths.Vec3(*unpack_result.unpacked_data),unpack_result.remaining_bytes)
def _unpack_unitary_quaternion(data: bytes):
    import Maths
    unpack_result = BytesPack.unpack_bytes_big_endian(["float","float","float"],data)
    x,y,z = unpack_result.unpacked_data
    diff = 1.0 - x * x - y * y - z * z;
    w = 0.0 if diff <= 0.0 else math.sqrt(diff)
    return (Maths.Quaternion(x,y,z,w),unpack_result.remaining_bytes)
def _unpack_variable1(data: bytes):
    unpacked_data,remaining = unpack_bytes_little_endian(["unsigned byte"],data)
    size = unpacked_data[0]
    return (remaining[0:size],remaining[size:])
def _unpack_variable2_be(data: bytes):
    unpacked_data,remaining = unpack_bytes_big_endian(["unsigned int16"],data)
    size = unpacked_data[0]
    return (remaining[0:size],remaining[size:])
def _unpack_variable2_le(data: bytes):
    unpacked_data,remaining = unpack_bytes_little_endian(["unsigned int16"],data)
    size = unpacked_data[0]
    return (remaining[0:size],remaining[size:])
def _unpack_fixed32(data: bytes):
    return (data[0:32],data[32:])


BytesPack._unpack_function_dict_be["vector3"] = _unpack_vector3
BytesPack._unpack_function_dict_be["vec3"] = _unpack_vector3
BytesPack._unpack_function_dict_be["vector3d"] = _unpack_vector3d
BytesPack._unpack_function_dict_be["vec3d"] = _unpack_vector3d
BytesPack._unpack_function_dict_be["unit_quaternion"] = _unpack_unitary_quaternion
BytesPack._unpack_function_dict_be["variable1"] = _unpack_variable1
BytesPack._unpack_function_dict_be["variable2"] = _unpack_variable2_be
BytesPack._unpack_function_dict_be["fixed32"] = _unpack_fixed32
BytesPack._unpack_function_dict_le["vector3"] = _unpack_vector3
BytesPack._unpack_function_dict_le["vec3"] = _unpack_vector3
BytesPack._unpack_function_dict_le["vector3d"] = _unpack_vector3
BytesPack._unpack_function_dict_le["vec3d"] = _unpack_vector3
BytesPack._unpack_function_dict_le["unit_quaternion"] = _unpack_unitary_quaternion
BytesPack._unpack_function_dict_le["variable1"] = _unpack_variable1
BytesPack._unpack_function_dict_le["variable2"] = _unpack_variable2_le
BytesPack._unpack_function_dict_le["fixed32"] = _unpack_fixed32

