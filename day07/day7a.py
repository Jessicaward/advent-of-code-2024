import re
from itertools import product

class Equation:
    def __init__(self, input: str):
        split_input = input.split(':')
        self.total = int(split_input[0])
        self.numbers = [int(num) for num in split_input[1].split(' ') if num != '']
    
    def print_equation(self):
        print(f"total: {self.total} with numbers: {self.numbers}")

def read_file(filename: str) -> list[Equation]:
    with open(filename, 'r') as file:
        return [Equation(line) for line in file.readlines()]
    
def generate_permutations(numbers: list[int]) -> list[str]:
    """ Generate every permutation of the operators and numbers (as a string so i can eval later) """
    possible_operators = ['*', '+']
    combinations = product(possible_operators, repeat=len(numbers) - 1)
    return [str(numbers[0]) + ''.join(
        [f"{op}{num}" for num, op in zip(numbers[1:], combination)]
    ) for combination in combinations]
    
def test_equation_possibilities(equation: Equation) -> bool:
    permutations = generate_permutations(equation.numbers)
    for permutation in permutations:
        if evaluate_left_to_right(permutation) == equation.total:
            return True
    return False

def evaluate_left_to_right(expression: str) -> int:
    """this challenge requires me to ignore bodmas and instead eval from l to r :):)"""
    tokens = re.findall('[+/*]|\d+',expression)
    result = int(tokens[0])
    for i in range(1, len(tokens), 2):
        operator = tokens[i]
        num = int(tokens[i + 1])
        
        if operator == '+':
            result += num
        elif operator == '*':
            result *= num
    return result

equations = read_file("input.txt")
valid_equations = [equation.total for equation in equations if test_equation_possibilities(equation)]
total_calibration_result = sum(valid_equations)

print(total_calibration_result)