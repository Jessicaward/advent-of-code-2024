import re

def read_file(filename: str) -> str:
    with open(filename) as f:
        return f.read()

def split_do(instructions: str) -> str:
    split_instructions = instructions.split("do")
    valid_instruction_lines = [line for line in split_instructions if not line.startswith("n't(")]
    return "".join(valid_instruction_lines)

def get_all_valid_instructions(instructions: str) -> list[str]:
    return re.findall(r'mul\(\d{1,3},\d{1,3}\)', instructions)

def get_left_and_right_operands(valid_instruction: str) -> tuple[int, int]:
    comma_seperated_operands = valid_instruction.replace("mul(", "").replace(')', '')
    split_operands = comma_seperated_operands.split(',')
    return split_operands[0], split_operands[1]

instructions = read_file("input.txt")
valid_instructions = split_do(instructions)
matches = get_all_valid_instructions(valid_instructions)
pairs = [get_left_and_right_operands(match) for match in matches]
multiplied_pairs = [int(pair[0]) * int(pair[1]) for pair in pairs]
sum_of_multiplied_pairs = sum(multiplied_pairs)

print(sum_of_multiplied_pairs)