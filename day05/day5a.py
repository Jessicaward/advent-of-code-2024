def build_rules_and_updates(filename) -> tuple[list[str], list[str]]:
    with open(filename, 'r') as file:
        #file is in rules and updates, i'm returning the rules before the newline and the updates after it
        sections = file.read().split("\n\n")
        rules = sections[0].splitlines() if len(sections) > 0 else []
        updates = sections[1].splitlines() if len(sections) > 1 else []
    return rules, updates

def find_valid_updates(rules: list[list[int]], updates: list[list[int]]) -> list[list[str]]:
    valid_updates = []
    for update in updates:
        is_update_valid = True
        for rule in rules:
            if contains_item_pair(update, rule[0], rule[1]):
                if update.index(rule[0]) > update.index(rule[1]):
                    is_update_valid = False
                    break
        if is_update_valid:
            valid_updates.append(update)
    
    return valid_updates

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

print(updates[0])

# Get all the valid update lists
valid_updates = find_valid_updates(rules, updates)
middle_numbers = get_middle_numbers_from_updates(valid_updates)
print(sum(middle_numbers))