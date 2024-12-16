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

def part1(input: tuple[list[str], list[str]]) -> int:
    def correct_page(page, tail, rules_dict):
        rule = rules_dict.get(page, None)

        if not rule:
            return tail == [page] or not tail

        return all([t in rule for t in tail])
            
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
        tail = pages_to_update[1:]
        correct_update = True
        
        for page in pages_to_update.copy():
            if not tail:
                break
                
            if not correct_page(page, tail, rules_dict):
                correct_update = False
                break

            tail = tail[1:]

        if correct_update:
            sum += pages_to_update[len(pages_to_update) // 2]
    
    return sum


input_test = process_input(get_input('Day05_test'))
output_part_1_test = part1(input_test)
assert output_part_1_test == 143, f'{output_part_1_test}'

input = process_input(get_input('Day05'))
output_part_1 = part1(input)
assert output_part_1 == 4924, f'{output_part_1}'
print(output_part_1)
