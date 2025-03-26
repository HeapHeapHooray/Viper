from template_parsing import *
from pathlib import Path
import os

#def tuple_block_definition(block):
#    definition = f"""{block.get_name()} = collections.namedtuple("{block.get_name()}",["""
#    for variable in block.get_variables():
#            definition = definition + '"'+variable.name+'"' +","
#    definition = definition + "])"

#    return definition


def block_definition(block):
    definition = f"""@dataclass\nclass {block.get_name()}:\n"""
    for variable in block.get_variables():
        definition = definition + f"""\t{variable.name}: "{variable.type}"\n"""

    return definition

type_mapping_dict = {"U8": "unsigned byte","U16": "unsigned int16",
                     "U32": "unsigned int32","U64": "unsigned int64",
                     "S8": "signed byte","S16": "signed int16","S32": "signed int32",
                     "S64": "signed int64","F32": "float","LLVector3": "vector3","LLVector3d": "vector3d",
                     "LLVector4": "vector4", "LLQuaternion": "unit_quaternion","LLUUID": "uuid","BOOL": "unsigned byte",
                     "Variable 1": "variable1","Variable 2": "variable2","F64": "double","Fixed 4": "unsigned int32","Fixed 32":"fixed32",
                     "IPADDR": "unsigned int32","IPPORT": "unsigned int16"}

def single_unpacking(block,unpacking_body):
    block_unpack_start = f"\n\t\tunpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["
    block_unpack_types = ""
    for variable in block.get_variables():
        block_unpack_types = block_unpack_types + f'"{type_mapping_dict[variable.type]}",'
    unpacking_body = unpacking_body + block_unpack_start + block_unpack_types + "],remaining_bytes)"
    unpacking_body = unpacking_body + f"\n\t\tself.{block.get_name()} = {block.get_name()}(*unpacked_data)\n"
    return unpacking_body

def multiple_unpacking(block,unpacking_body):
    unpacking_body = unpacking_body+f"\n\t\tfor i in range(blocks_count):\n\t\t\tunpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["
    block_unpack_types = ""
    for variable in block.get_variables():
        block_unpack_types = block_unpack_types + f'"{type_mapping_dict[variable.type]}",'
    unpacking_body = unpacking_body+block_unpack_types+"],remaining_bytes)"
    unpacking_body = unpacking_body+f"\n\t\t\tself.{block.get_name()}.append({block.get_name()}(*unpacked_data))\n"

    return unpacking_body
def generate_message_class(message):
    info = """# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper"""
    
    imports = "from Message.Message import Message\nimport BytesUtils\nfrom dataclasses import dataclass"

    blocks = message.get_message_blocks()

    # Creates namedtuples for each block type.
    blocks_definition = ""
    for block in blocks:
        blocks_definition = blocks_definition + block_definition(block) + "\n"

    # Class Header with Absolute ID of the Message.
    class_header = f"class {message.get_message_name()}(Message):\n\n\tabsolute_id = {message.get_message_absolute_id()} # -- The Full ID of the message"

    # Header of __init__ function.
    init = "\n\tdef __init__(self,bytes_data: bytes):"

    # Initializes all blocks with None values.
    for block in blocks:
        amount = 0
        MultipleBlock = False
        VariableBlock = False
        if block.get_quantity().startswith("Variable"):
            VariableBlock = True
        if block.get_quantity().startswith("Multiple"):
            MultipleBlock = True
            amount = int(block.get_quantity().split(" ")[1])
        if VariableBlock:
            init = init + f"\n\t\tself.{block.get_name()} = [{block.get_name()}(*((None,)*{len(block.get_variables())}))]"
        elif MultipleBlock and amount:
            init = init + f"\n\t\tself.{block.get_name()} = []"
            init = init + f"\n\t\tfor i in range({amount}):\n\t\t\tself.{block.get_name()}.append({block.get_name()}(*((None,)*{len(block.get_variables())})))"
        else:
            init = init + f"\n\t\tself.{block.get_name()} = {block.get_name()}(*((None,)*{len(block.get_variables())}))"

    # Return if bytes_data is None, i.e. there is nothing to load, and since everything is initialized to None we can return already.
    init = init + "\n\n\t\tif bytes_data is None:\n\t\t\treturn"

    unpacking_body = "\n\t\tremaining_bytes = bytes_data\n"
    for block in blocks:
        amount = 0
        VariableBlock = False
        MultipleBlock = False
        if block.get_quantity().startswith("Variable"):
            VariableBlock = True
            unpacking_body = unpacking_body + f"""\n\t\tunpacked_data,remaining_bytes = BytesUtils.unpack_bytes_little_endian(["unsigned byte"],remaining_bytes)"""
            unpacking_body = unpacking_body + f"\n\t\tblocks_count = unpacked_data[0] # -- Variable Blocks length is encoded in the message as a single byte.\n\n\t\tself.{block.get_name()} = []\n"
        if block.get_quantity().startswith("Multiple"):
            MultipleBlock = True
            amount = int(block.get_quantity().split(" ")[1])
            unpacking_body = unpacking_body + f"\n\t\tblocks_count = {amount} # -- Fixed/constant Blocks length of {amount}. \n\n\t\tself.{block.get_name()} = []\n"

        if VariableBlock or MultipleBlock:
            unpacking_body = multiple_unpacking(block,unpacking_body)
        else:
            unpacking_body = single_unpacking(block,unpacking_body)
        
    convert_to_string = "\n\tdef convert_to_string(self) -> str:"

    convert_to_string = convert_to_string + f'\n\t\treturn f"""Message Type: {message.get_message_name()}, \nMessage Absolute ID: {message.get_message_absolute_id()}\nBlocks:'


    for block in blocks:
        convert_to_string = convert_to_string + f'\n{"{"+"self."+block.get_name()+"}"}'

    convert_to_string = convert_to_string + '"""'

    convert_to_bytes = "\n\tdef convert_to_bytes(self) -> bytes:"

    convert_to_bytes = convert_to_bytes+'\n\t\toutput = b""\n'

    for block in blocks:
        VariableBlock = False
        MultipleBlock = False
        if block.get_quantity().startswith("Variable"):
            VariableBlock = True
            convert_to_bytes = convert_to_bytes + f"""\n\t\tblocks_count = len(self.{block.get_name()})\n\t\toutput = output + BytesUtils.pack_bytes_little_endian(["unsigned byte"],blocks_count)\n"""
        if block.get_quantity().startswith("Multiple"):
            MultipleBlock = True
            amount = int(block.get_quantity().split(" ")[1])
            convert_to_bytes = convert_to_bytes + f"\n\t\tblocks_count = {amount}\n"

        if VariableBlock or MultipleBlock:
            convert_to_bytes = convert_to_bytes + "\n\t\tfor i in range(blocks_count):\n\t\t\toutput = output + BytesUtils.pack_bytes_little_endian(["
            for variable in block.get_variables():
                convert_to_bytes = convert_to_bytes + f'"{type_mapping_dict[variable.type]}",'
            convert_to_bytes = convert_to_bytes + "]"
            for variable in block.get_variables():
                convert_to_bytes = convert_to_bytes + f",self.{block.get_name()}[i].{variable.name}"
            convert_to_bytes = convert_to_bytes + ")\n"
        else:
            convert_to_bytes = convert_to_bytes+"\n\t\toutput = output + BytesUtils.pack_bytes_little_endian(["
            for variable in block.get_variables():
                convert_to_bytes = convert_to_bytes + f'"{type_mapping_dict[variable.type]}",'
            convert_to_bytes = convert_to_bytes + "]"
            for variable in block.get_variables():
                convert_to_bytes = convert_to_bytes + f",self.{block.get_name()}.{variable.name}"
            convert_to_bytes = convert_to_bytes + ")\n"

    convert_to_bytes = convert_to_bytes + "\n\t\treturn output"
    
    return info+"\n\n"+imports+"\n\n"+blocks_definition+"\n"+class_header+"\n"+init+"\n"+unpacking_body+"\n"+convert_to_string+"\n"+convert_to_bytes
            
def generate_code():
    print("Generating Code...")
    
    messages = get_messages()

    try:
        messages_dir = Path("./Messages")
        os.mkdir(messages_dir)
    except FileExistsError:
        pass


    messages_init_py_header = "# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper\n"
    decoder_header = """# This code is automatically generated for the Viper viewer project, and the generation code can be found at: https://github.com/HeapHeapHooray/Viper\nfrom Messages import *

_id_to_class = {}



def get_message_class_from_id(message_id: int):
    return _id_to_class.get(message_id,None)

def _load_message_class(message_class):
    _id_to_class[message_class.absolute_id] = message_class"""

    successful = []
    for message in messages:
        try:
            generated = generate_message_class(message)
            name = message.get_message_name()
            with open(Path("./Messages/"+name+".py"),"w") as message_file:
                message_file.write(generated)
            successful.append(name)
        except e:
            print("Raised exception:",e)

    decoder = decoder_header + "\n\n" + "\n".join("_load_message_class("+name+"."+name+")" for name in successful)

    try:
        message_dir = Path("./Message")
        os.mkdir(message_dir)
    except FileExistsError:
        pass

    with open(Path("./Message/MessageDecoder.py"),"w") as decoder_file:
        decoder_file.write(decoder)
    messages_init_py = messages_init_py_header + "\n" + "\n".join(("from . import "+name) for name in successful)
    with open(Path("./Messages/__init__.py"),"w") as messages_init_py_file:
        messages_init_py_file.write(messages_init_py)

if __name__ == "__main__":
    generate_code()
