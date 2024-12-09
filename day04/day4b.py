def build_char_matrix_from_input(filename: str) -> list[list[str]]:
    with open(filename, 'r') as file:
        rows = file.read().splitlines()
        return [list(col) for col in rows]
    
def find_number_of_patterns(matrix: list[list[str]]) -> int:
    count = 0
    for x_index in range(len(matrix) - 2):
        for y_index in (range(len(matrix[x_index + 1]) - 2)):
            # Define x and y as one higher as we only care about the inner square
            x = x_index + 1
            y = y_index + 1
            current_char = matrix[x][y]
            if current_char == "A":
                if does_pattern_exist_in_diagonal(matrix, x, y):
                    count = count + 1
    return count

def does_pattern_exist_in_diagonal(matrix: list[list[str]], x_index: int, y_index: int) -> bool:
    allowed_chars = ['M', 'S']
    if not contains_item(allowed_chars, matrix[x_index-1][y_index-1]) or not contains_item(allowed_chars, matrix[x_index+1][y_index+1]):
        # One of the diagonal items does not match M or S
        return False
    if matrix[x_index-1][y_index-1] == matrix[x_index+1][y_index+1]:
        # They matched, but they're the same
        return False
    if not contains_item(allowed_chars, matrix[x_index-1][y_index+1]) or not contains_item(allowed_chars, matrix[x_index+1][y_index-1]):
        # One of the other diagonal items does not match M or S
        return False
    if matrix[x_index-1][y_index+1] == matrix[x_index+1][y_index-1]:
        # They matched, but they're the same
        return False
    return True

def contains_item(list_to_check: list, item_to_check: str):
    return any(x in item_to_check for x in list_to_check)
    
filename = "input.txt"
char_matrix = build_char_matrix_from_input(filename)
count = find_number_of_patterns(char_matrix)

print(count)
# 2010 is too high