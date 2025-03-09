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
BytesPack._type_minimum_sizes["unit_quaternion"] = 12

def _pack_vector3(vec3):
    return vec3.convert_to_bytes()
def _pack_unitary_quaternion(quat):
    return quat.convert_to_bytes()

BytesPack._pack_function_dict_be["vector3"] = _pack_vector3
BytesPack._pack_function_dict_be["vec3"] = _pack_vector3
BytesPack._pack_function_dict_be["unit_quaternion"] = _pack_unitary_quaternion
BytesPack._pack_function_dict_le["vector3"] = _pack_vector3
BytesPack._pack_function_dict_le["vec3"] = _pack_vector3
BytesPack._pack_function_dict_le["unit_quaternion"] = _pack_unitary_quaternion

def _unpack_vector3(data: bytes):
    import Maths
    unpack_result = BytesPack.unpack_bytes_big_endian(["float","float","float"],data)
    return (Maths.Vec3(*unpack_result.unpacked_data),unpack_result.remaining_bytes)
def _unpack_unitary_quaternion(data: bytes):
    import Maths
    unpack_result = BytesPack.unpack_bytes_big_endian(["float","float","float"],data)
    x,y,z = unpack_result.unpacked_data
    diff = 1.0 - x * x - y * y - z * z;
    w = 0.0 if diff <= 0.0 else math.sqrt(diff)
    return (Maths.Quaternion(x,y,z,w),unpack_result.remaining_bytes)


BytesPack._unpack_function_dict_be["vector3"] = _unpack_vector3
BytesPack._unpack_function_dict_be["vec3"] = _unpack_vector3
BytesPack._unpack_function_dict_be["unit_quaternion"] = _unpack_unitary_quaternion
BytesPack._unpack_function_dict_le["vector3"] = _unpack_vector3
BytesPack._unpack_function_dict_le["vec3"] = _unpack_vector3
BytesPack._unpack_function_dict_le["unit_quaternion"] = _unpack_unitary_quaternion 

