import BytesUtils

class Vec3:
    def __init__(self,x: float,y: float,z: float):
        self.x = x
        self.y = y
        self.z = z
    def convert_to_string(self) -> str:
        return "Vector3 <X: {}, Y: {}, Z: {}>".format(self.x,self.y,self.z)
    def convert_to_bytes(self) -> bytes:
        return BytesUtils.pack_bytes(["float","float","float"],self.x,self.y,self.z)
