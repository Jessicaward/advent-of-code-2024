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
    # TODO: I've been thinking and I reckong there is a huge optimisation here 
    # TODO: since each operator increases the value of the result (there is no - or /, so it doesn't decrease)
    # TODO: instead of generating each permutation then testing it, we could instead generate each section
    # TODO: if the current result after adding the operator is above the total, it cannot possibly be a valid route, so we should backtrack
    possible_operators = ['*', '+', '||']
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
    tokens = re.findall('[+/*]|\d+|\|\|',expression)
    result = int(tokens[0])
    previous_token = tokens[0]

    for i in range(1, len(tokens), 2):
        num = int(tokens[i + 1])
        if previous_token.isdigit() and tokens[i].isdigit():
            raise ValueError("invalid sum")
        if tokens[i] == '+':
            result += num
        elif tokens[i] == '*':
            result *= num
        elif tokens[i] == "||":
            result = int(str(result) + str(num))
    return result

equations = read_file("input.txt")
valid_equations = [equation.total for equation in equations if test_equation_possibilities(equation)]
total_calibration_result = sum(valid_equations)

print(total_calibration_result)