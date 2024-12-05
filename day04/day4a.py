# This was kinda cool but it could be improved through d y n a m i c programming

from collections import defaultdict

def build_char_matrix_from_input(filename: str) -> list[list[str]]:
    with open(filename, 'r') as file:
        rows = file.read().splitlines()
        return [list(col) for col in rows]

def find_substring_count_in_inputs(substring: str, strings_to_search: list[str]) -> int:
    return sum([x.count(substring) for x in strings_to_search])

def reverse_list_in_place(input: list) -> list:
    return input[::-1]

def flatten_matrix(matrix: list[list[str]]) -> list[str]:
    return [s for l in matrix for s in l]

# I stole this function from https://stackoverflow.com/a/43311126
def build_diagonal_from_matrix(matrix: list[list[str]], func):
    grouping = defaultdict(list)
    for y in range(len(matrix)):
        for x in range(len(matrix[y])):
            grouping[func(x, y)].append(matrix[y][x])
    return [''.join(grouping[key]) for key in sorted(grouping)]

# 8 different ways of reading the data
def read_matrix_across_left_to_right(matrix: list[list[str]]) -> list[str]:
    return ["".join(char_list) for char_list in matrix]

def read_matrix_across_right_to_left(matrix: list[list[str]]) -> list[str]:
    return ["".join(reverse_list_in_place(char_list)) for char_list in matrix]

def read_matrix_down(matrix: list[list[str]]) -> list[str]:
    return [
        "".join([row[column_index] for row in matrix]) for column_index in range(len(matrix[0]))
    ]

def read_matrix_up(matrix: list[list[str]]) -> list[str]:
    return [
        "".join(reverse_list_in_place([row[column_index] for row in matrix])) for column_index in range(len(matrix[0]))
    ]

def read_matrix_tl_br(matrix: list[list[str]]) -> list[str]:
    return [reverse_list_in_place(x) for x in build_diagonal_from_matrix(matrix, lambda x, y: x + y)]

def read_matrix_tr_bl(matrix: list[list[str]]) -> list[str]:
    return build_diagonal_from_matrix(matrix, lambda x, y: y - x)

def read_matrix_bl_tr(matrix: list[list[str]]) -> list[str]:
    return [reverse_list_in_place(x) for x in build_diagonal_from_matrix(matrix, lambda x, y: x - y)]

def read_matrix_br_tl(matrix: list[list[str]]) -> list[str]:
    return reverse_list_in_place([reverse_list_in_place(x) for x in read_matrix_tl_br(matrix)])

interpretations = [
    read_matrix_across_left_to_right,
    read_matrix_across_right_to_left,
    read_matrix_down,
    read_matrix_up,
    read_matrix_tl_br,
    read_matrix_tr_bl,
    read_matrix_bl_tr,
    read_matrix_br_tl
]

filename = "input.txt"
char_matrix = build_char_matrix_from_input(filename)
search_strings = flatten_matrix([interpretation(char_matrix) for interpretation in interpretations])
count_of_xmas = find_substring_count_in_inputs("XMAS", search_strings)

print(count_of_xmas)