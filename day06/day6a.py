from itertools import takewhile

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def print_position(self):
        print(f"x: {self.x} - y: {self.y}")
    
    def __hash__(self):
        return hash((self.x, self.y))

    def __eq__(self, other):
        if isinstance(other, Position):
            return self.x == other.x and self.y == other.y
        return False

class Chart:
    def __init__(self, filename: str):
        self.chart = self.build_chart_from_file(filename)

    def build_chart_from_file(self, filename: str) -> list[list[str]]:
        with open(filename, 'r') as file:
            return [list(takewhile(lambda c: c != '\n', row)) for row in file.readlines()]
    
    def switch_items(self, first_position: Position, second_position: Position):
        if first_position == second_position:
            raise ValueError("first_position cannot be the same as second_position")
        
        original_item = self.chart[first_position.x][first_position.y]
        self.chart[first_position.x][first_position.y] = self.chart[second_position.x][second_position.y]
        self.chart[second_position.x][second_position.y] = original_item

    def get_element_at_position(self, position: Position) -> str:
        return self.chart[position.x][position.y]
    
    def print(self):
        for row in self.chart:
            for item in row:
                print(item, end='')
            print()
    
    def find_guard(self) -> tuple[Position, str]:
        """Returns the position and character of the guard"""
        guard_chars = ['<', '>', '^', 'V']
        for row_index in range(len(self.chart)):
            for col_index in range(len(self.chart[row_index])):
                if any(self.chart[row_index][col_index] in char for char in guard_chars):
                    return Position(row_index, col_index), self.chart[row_index][col_index]

def simulate_guard_movement(chart: Chart) -> Position:
    """ Returns new position for guard """
    guard_details = chart.find_guard()
    current_position = guard_details[0]
    guard_character = guard_details[1]
    next_position = get_next_position_for_guard(current_position, guard_character)

    next_element = chart.get_element_at_position(next_position)
    if next_element == "#":
        # Rotate, can't move!
        chart.chart[current_position.x][current_position.y] = turn_90_degrees(guard_character)
        return current_position
    elif next_element == ".":
        # Move forward
        chart.switch_items(current_position, next_position)
        return next_position

def get_next_position_for_guard(guard_position: Position, guard_character: str) -> Position:
    match guard_character:
        case 'V':
            return Position(guard_position.x + 1, guard_position.y)
        case '^':
            return Position(guard_position.x - 1, guard_position.y)
        case '<':
            return Position(guard_position.x, guard_position.y - 1)
        case '>':
            return Position(guard_position.x, guard_position.y + 1)
        case _:
            raise ValueError("This is not a guard, can't get next position")
        
def turn_90_degrees(guard_character: str) -> str:
    match guard_character:
        case '^':
            return '>'
        case '>':
            return 'V'
        case 'V':
            return '<'
        case '<':
            return '^'
        case _:
            raise ValueError("This is not a guard, can't rotate")

chart = Chart("input.txt")
unique_positions = set()
starting_position_details = chart.find_guard()
unique_positions.add(starting_position_details[0])

while True:
    is_out_of_bounds = False
    try:
        new_position = simulate_guard_movement(chart)

        if new_position == starting_position_details[0] and chart.find_guard()[1] == starting_position_details[1]:
            # if we're back at the start, there are no more unique positions left
            break
            
        unique_positions.add(new_position)

    except IndexError:
        is_out_of_bounds = True
    
    if is_out_of_bounds:
        # if guard has left the map, there are no more unique positions left
        break

print(f"There are {len(unique_positions)} unique positions")