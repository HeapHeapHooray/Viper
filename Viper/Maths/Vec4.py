import BytesUtils

class Vec4:
    def __init__(self,x: float,y: float,z: float,w: float):
        self.x = x
        self.y = y
        self.z = z
        self.w = w
    def convert_to_string(self) -> str:
        return "Vector4 <X: {}, Y: {}, Z: {}, W: {}>".format(self.x,self.y,self.z,self.w)
    def __str__(self) -> str:
        return self.convert_to_string()
    def __repr__(self) -> str:
        return self.convert_to_string()
    def convert_to_bytes(self) -> bytes:
        return BytesUtils.pack_bytes_big_endian(["float","float","float","float"],self.x,self.y,self.z,self.w)
    def convert_as_doubles_to_bytes(self) -> bytes:
        return BytesUtils.pack_bytes_big_endian(["double","double","double","double"],self.x,self.y,self.z,self.w)
