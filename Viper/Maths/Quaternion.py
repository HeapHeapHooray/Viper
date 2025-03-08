import BytesUtils

class Quaternion:
    def __init__(self,x: float,y: float,z: float,w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    def convert_to_string(self) -> str:
        return "Quaternion <X: {}, Y: {}, Z: {}, W: {}>".format(self.x,self.y,self.z,self.w)
    def convert_to_bytes(self) -> bytes:
        # Since this will always be an unit quaternion we omit the w value from the
        # representation in bytes, since it can be inferred from the other values.
        return BytesUtils.pack_bytes_big_endian(["float","float","float"],self.x,self.y,self.z)
