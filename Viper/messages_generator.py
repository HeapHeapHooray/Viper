from parse_message_template import *

def tuple_block_definition(block):
    definition = f"""{block.get_name()} = collections.namedtuple("{block.get_name()}",["""
    for variable in block.get_variables():
            definition = definition + '"'+variable.name+'"' +","
    definition = definition + "])"

    return definition

type_mapping_dict = {"U8": "unsigned byte","U16": "unsigned int16",
                     "U32": "unsigned int32","U64": "unsigned int64",
                     "S8": "signed byte","S16": "signed int16","S32": "signed int32",
                     "S64": "signed int64","F32": "float","LLVector3": "vector3",
                     "LLQuaternion": "unit_quaternion","LLUUID": "uuid","BOOL": "unsigned byte",
                     "Variable 1": "variable1","Variable 2": "variable2","F64": "double","Fixed 4": "unsigned int32","Fixed 32":"fixed32"}

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
    info = """# This code has been automatically generated, the generation code is named "messages_generator.py"."""
    
    imports = "from Message.Message import Message\nimport BytesUtils\nimport collections"

    blocks = message.get_message_blocks()

    # Creates namedtuples for each block type.
    blocks_definition = ""
    for block in blocks:
        blocks_definition = blocks_definition + tuple_block_definition(block) + "\n"

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
            

