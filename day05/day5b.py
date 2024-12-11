from collections import deque, defaultdict

def build_rules_and_updates(filename) -> tuple[list[str], list[str]]:
    with open(filename, 'r') as file:
        #file is in rules and updates, i'm returning the rules before the newline and the updates after it
        sections = file.read().split("\n\n")
        rules = sections[0].splitlines() if len(sections) > 0 else []
        updates = sections[1].splitlines() if len(sections) > 1 else []
    return rules, updates

def find_invalid_updates(rules: list[list[int]], updates: list[list[int]]) -> list[list[str]]:
    invalid_updates = []
    for update in updates:
        is_update_valid = True
        for rule in rules:
            if contains_item_pair(update, rule[0], rule[1]):
                if update.index(rule[0]) > update.index(rule[1]):
                    is_update_valid = False
                    break
        if not is_update_valid:
            invalid_updates.append(update)
    return invalid_updates

def fix_update(rules: list[list[int]], update: list[int]) -> list[int]:
    # this uses topological sorting (the thing that lets excel cells work :)) as the constaints all rely on each other
    graph = defaultdict(list)
    in_degree = {page: 0 for page in update}
    
    for rule in rules:
        if rule[0] in update and rule[1] in update:
            graph[rule[0]].append(rule[1])
            in_degree[rule[1]] += 1
    
    # perform topological sort here
    queue = deque([node for node in update if in_degree[node] == 0])
    sorted_update = []
    
    while queue:
        current = queue.popleft()
        sorted_update.append(current)
        
        for neighbor in graph[current]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    
    return sorted_update

def move_item_before(list_to_update: list[int], from_index: int, before_index: int) -> list[int]:
    item = list_to_update.pop(from_index)
    list_to_update.insert(before_index, item)
    return list_to_update

def fix_updates(rules: list[list[int]], updates: list[list[int]]) -> list[list[int]]:
    return [fix_update(rules, update) for update in updates]

def parse_rules(rules: list[str]) -> list[list[int]]:
    return [list(map(int, rule.split('|'))) for rule in rules]

def parse_updates(updates: list[str]) -> list[list[int]]:
    return [list(map(int, update.split(','))) for update in updates]

def contains_item_pair(list_to_check: list[int], first_item: int, second_item: int) -> bool:
    items = set(list_to_check)
    return first_item in items and second_item in items

def get_middle_numbers_from_updates(updates: list[list[int]]) -> list[int]:
    return [update[int((len(update) - 1) / 2)] for update in updates]

unparsed_rules, unparsed_updates = build_rules_and_updates("input.txt")

rules = parse_rules(unparsed_rules)
updates = parse_updates(unparsed_updates)
invalid_updates = find_invalid_updates(rules, updates)
fixed_updates = fix_updates(rules, invalid_updates)
print(sum(get_middle_numbers_from_updates(fixed_updates)))