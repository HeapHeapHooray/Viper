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
