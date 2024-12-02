def build_reports(filename) -> list:
    with open(filename, 'r') as file:
        return [[int(num) for num in line.split()] for line in file]
    
def is_safe(report: list[int]) -> bool:
    return all_same_direction(report) and is_value_jump_safe(report)

def is_value_jump_safe(report: list[int]) -> bool:
    for level_index in range(0, len(report) - 1):
        if abs(report[level_index]-report[level_index + 1]) > 3:
            return False
    return True

def all_same_direction(report: list[int]) -> bool:
    if report[0] == report[1]:
        # neither increasing, nor decreasing, unsafe!
        return False
    
    is_increasing = report[0] < report[1]

    for level_index in range(0, len(report) - 1):
        if is_increasing:
            if report[level_index] >= report[level_index + 1]:
                return False
        else:
            if report[level_index] <= report[level_index + 1]:
                return False
    
    return True

reports = build_reports("input.txt")
number_of_safe_reports = 0

for report in reports:
    if is_safe(report):
        number_of_safe_reports += 1

print(number_of_safe_reports)