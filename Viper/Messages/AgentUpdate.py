from Message.Message import Message
import BytesUtils

class AgentUpdate(Message):
    absolute_id = 4
    force_zerocode = True
    def __init__(self,bytes_data: bytes):
        self.agent_uuid,self.session_uuid,self.body_rotation,self.head_rotation,self.state,self.camera_center,self.camera_at_axis,self.camera_left_axis,self.camera_up_axis,self.far,self.control_flags,self.flags= [None,None,None,None,None,None,None,None,None,None,None,None]
        if bytes_data is None:
            return
        result = BytesUtils.unpack_bytes_little_endian(["uuid","uuid","unit_quaternion","unit_quaternion",
                                                        "unsigned byte","vector3","vector3","vector3"
                                                        ,"vector3","float","unsigned int32","unsigned byte"],bytes_data)
        self.agent_uuid,self.session_uuid,self.body_rotation,self.head_rotation,
        self.state,self.camera_center,self.camera_at_axis,
        self.camera_left_axis,self.camera_up_axis,self.far,
        self.control_flags,self.flags = result.unpacked_data
    def convert_to_string(self) -> str:
        return "Message Type: AgentUpdate , Message Absolute ID: {} , Agent UUID: {} , Session UUID: {} , Body Rotation: {} , Head Rotation: {} , State: {} , Camera Center: {} , Camera At Axis: {} , Camera Left Axis: {} , Camera Up Axis: {} , Far: {} , Control Flags: {}, Flags: {}".format(AgentUpdate.absolute_id, self.agent_uuid,self.session_uuid,self.body_rotation,self.head_rotation,self.state,self.camera_center,self.camera_at_axis,self.camera_left_axis,self.camera_up_axis,self.far,self.control_flags,self.flags)
    def convert_to_bytes(self) -> bytes:
        return BytesUtils.pack_bytes_little_endian(["uuid","uuid","unit_quaternion","unit_quaternion",
                                                        "unsigned byte","vector3","vector3","vector3"
                                                        ,"vector3","float","unsigned int32","unsigned byte"],self.agent_uuid,self.session_uuid,self.body_rotation,self.head_rotation,self.state,self.camera_center,self.camera_at_axis,self.camera_left_axis,self.camera_up_axis,self.far,self.control_flags,self.flags)
