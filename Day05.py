from utils import get_input
import re


def process_input(input: list[str]) -> tuple[list[str], list[str]]:
    rules = []
    updates = []
    reading_rules = True

    for line in input:
        if reading_rules:
            if not re.match('\s+', line):
                rules.append(line.strip())
            else:
                reading_rules = False
        else:
            updates.append(line.strip())

    return rules, updates

def is_correct_update(pages_to_update: list[int], rules_dict: dict[int, list[int]]) -> bool:
    def correct_page(page, tail, rules_dict):
        rule = rules_dict.get(page, None)

        if not rule:
            return tail == [page] or not tail

        return all([t in rule for t in tail])

    tail = pages_to_update[1:]
    
    for page in pages_to_update.copy():
        if not tail:
            break
            
        if not correct_page(page, tail, rules_dict):
            return False

        tail = tail[1:]

    return True

def part1(input: tuple[list[str], list[str]]) -> int:
    sum = 0
    rules, updates = input
    rules_dict = dict()

    for rule in rules:
        p1, p2 = [int(x) for x in rule.split('|')[:2]]
        if p1 not in rules_dict:
            rules_dict[p1] = [p2]
        else:
            rules_dict[p1].append(p2)

    for update in updates:
        pages_to_update = [int(x) for x in update.split(',')]

        if is_correct_update(pages_to_update, rules_dict):
            sum += pages_to_update[len(pages_to_update) // 2]
    
    return sum


def part2(input) -> int:
    def correct_page(pages, page_idx, rules_dict):
        rule = rules_dict.get(pages[page_idx], None)

        if not rule:
            return page_idx in (len(pages), len(pages) - 1)

        return all([t in rule for t in pages[page_idx + 1:]])

    sum = 0
    rules, updates = input
    rules_dict = dict()

    for rule in rules:
        p1, p2 = [int(x) for x in rule.split('|')[:2]]
        if p1 not in rules_dict:
            rules_dict[p1] = [p2]
        else:
            rules_dict[p1].append(p2)

    incorrect_updates = []

    for update in updates:
        pages_to_update = [int(x) for x in update.split(',')]

        if not is_correct_update(pages_to_update, rules_dict):
            incorrect_updates.append(pages_to_update)

    for update in incorrect_updates:
        incorrect_page_idx = 0
        sorted_update = update.copy()

        while incorrect_page_idx < len(sorted_update):
            while not correct_page(sorted_update, incorrect_page_idx, rules_dict):
                el = sorted_update.pop(incorrect_page_idx)
                sorted_update.append(el)

            incorrect_page_idx += 1

        sum += sorted_update[len(sorted_update) // 2]

    return sum

input_test = process_input(get_input('Day05_test'))
output_part_1_test = part1(input_test)
assert output_part_1_test == 143, f'{output_part_1_test}'

input = process_input(get_input('Day05'))
output_part_1 = part1(input)
assert output_part_1 == 4924, f'{output_part_1}'
print(output_part_1)

output_part_2_test = part2(input_test)
assert output_part_2_test == 123, f'{output_part_2_test}'

output_part_2 = part2(input)
assert output_part_2 == 6085, f'{output_part_2}'
print(output_part_2)
