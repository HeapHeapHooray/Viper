from collections import namedtuple
from typing import List
message_template_default_name = "message_template.msg"

class BlockTree:
    def __init__(self,parent):
        self._parent = parent
        self.children = []
        self.entry_data = ""
        self.pre_entry_data = ""
        self.inner_data = ""
        self.full_data = ""
        self.start_index = -1
        self.end_index = -1
    def add_child(self,child):
        self.children.append(child)
    def get_parent(self):
        if self._parent is None:
            return None
        return self._parent
    def get_full_block(self):
        result = self.entry_data
        for child in self.children:
            result = result + child.get_full_block()
        return result

StructureElements = namedtuple("StructureElements","comment open_bracket close_bracket")
def detect_structure_elements(line: str):
    comment = line.find("//")
    open_bracket = line.find("{")
    close_bracket = line.find("}")

    return StructureElements(comment,open_bracket,close_bracket)

def has_valid_open_bracket(line: str):
    elements = detect_structure_elements(line)
    if elements.open_bracket == -1:
        return False
    if (elements.comment != -1) and elements.comment < elements.open_bracket:
        return False
    return True

def has_valid_close_bracket(line: str):
    elements = detect_structure_elements(line)
    if elements.close_bracket == -1:
        return False
    if (elements.comment != -1) and elements.comment < elements.close_bracket:
        return False
    return True

def parse_message_template(filename=message_template_default_name):
    file = open(filename,mode="r")
    data = file.read()
    lines = data.split("\n")
    current_block = None
    blocks = []

    for idx,line in enumerate(lines):
        if has_valid_open_bracket(line):
            if current_block == None:
                current_block = BlockTree(None)
                current_block.start_index = idx
                current_block.pre_entry_data = lines[idx-1]
                current_block.entry_data = line
                blocks.append(current_block)
            else:
                child = BlockTree(current_block)
                child.start_index = idx
                child.pre_entry_data = lines[idx-1]
                child.entry_data = line
                current_block.add_child(child)
                #blocks.append(child)
                current_block = child
        if has_valid_close_bracket(line) and current_block != None:
            current_block.end_index = idx
            current_block.inner_data = "\n".join(
                lines[current_block.start_index+1:current_block.end_index])
            current_block.full_data = "\n".join(
                lines[current_block.start_index-1:current_block.end_index+1])
            current_block = current_block.get_parent()
    return blocks

class Message:
    def __init__(self,block_tree):
        self._block_tree = block_tree
    def get_message_signature(self):
        unprocessed_signature = self._block_tree.inner_data
        try:
            unprocessed_signature = self._block_tree.children[0].pre_entry_data
        except IndexError as e:
            pass
        return unprocessed_signature.strip()
    def get_message_signature_as_list(self):
        return self.get_message_signature().split()
    def get_message_name(self):
        return self.get_message_signature_as_list()[0]
    def get_message_frequency(self):
        return self.get_message_signature_as_list()[1]
    def get_message_relative_id(self):
        raw_relative_id = self.get_message_signature_as_list()[2]
        frequency = self.get_message_frequency()

        if frequency == "Fixed":
            relative_id = int(raw_relative_id,16)
        else:
            relative_id = int(raw_relative_id,10)

        return relative_id
    def get_message_absolute_id(self):
        frequency = self.get_message_frequency()
        relative_id = self.get_message_relative_id()

        if frequency == "Fixed":
            absolute_id = relative_id
        elif frequency == "Low":
            absolute_id = int("FFFF0000",16) + relative_id
        elif frequency == "Medium":
            absolute_id = int("FF00",16) + relative_id
        else:
            absolute_id = relative_id

        return absolute_id
    def get_message_blocks(self):
        output = []
        for child in self._block_tree.children:
            output.append(MessageBlock(child))
        return output

def get_messages():
    blocks = parse_message_template()
    messages = [Message(block_tree) for block_tree in blocks]
    return messages

def get_messages_by_absolute_id():
    messages_dict = {}
    for message in get_messages():
        messages_dict[message.get_message_absolute_id()] = message
    return messages_dict

class MessageBlock:
    def __init__(self,block: BlockTree):
        self._block_tree = block
    def _get_lines(self):
        return self._block_tree.inner_data.strip("\n").split("\n")
    def get_signature(self):
        lines = self._get_lines()
        stripped = lines[0].strip()
        comment_slashes = stripped.find("//")
        if comment_slashes >= 0:
            stripped = stripped[0:comment_slashes]
        return stripped
    def get_signature_as_list(self):
        return [element.strip() for element in (self.get_signature().split(" ")) if len(element)]
    def get_name(self):
        return self.get_signature_as_list()[0]
    def get_quantity(self):
        sig = self.get_signature_as_list()
        return " ".join(sig[1::])
    def get_variables(self):
        lines = self._get_lines()
        variables = []
        for line in lines[1::]:
            close_bracket = line.find("}")
            if close_bracket >= 0:
                line = line[0:close_bracket]
            preprocessed = line.strip()
            if not preprocessed.startswith("{"):
                print("Ignoring:\n",preprocessed)
                continue
            lst = preprocessed.strip("{").strip().split(" ")
            processed_lst = [e for e in lst if len(e) > 0]
            if len(processed_lst):
                variables.append(Variable(processed_lst))
        return variables
    
class Variable:
    def __init__(self,fragments: List[str]):
        self.name = fragments[0]
        self.type = " ".join(fragments[1::])
    def convert_to_string(self):
        return f"< Name: {self.name} | Type: {self.type} >"
    def __str__(self):
        return self.convert_to_string()
    def __repr__(self):
        return self.convert_to_string()
        
    
def parse_inner_block(block: BlockTree):
    raw_data = block.inner_data
    open_bracket = raw_data.find("{")
    close_bracket = raw_data.find("}")
    if open_bracket < 0 or close_bracket < 0:
        return ""
    
    block_signature = raw_data[0:open_bracket]
    block_signature_as_list = block_signature.strip().split(" ")
    return block_signature_as_list


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
    info = """# This code has been automatically generated, the generation code is in the message template parser for now."""
    
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
            
