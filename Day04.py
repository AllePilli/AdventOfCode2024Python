from utils import get_input

DIR_DELTAS = [
    (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1)
]


def count_word(x: int, y: int, word: str, input: list[str]) -> int:
    dim_y = len(input)
    dim_x = len(input[0])
    count = 0

    for delta in DIR_DELTAS:
        for i, c in enumerate(word[1:], start=1):
            cx, cy = x + i * delta[0], y + i * delta[1]
            if cx < 0 or cx >= dim_x or cy < 0 or cy >= dim_y or c != input[cy][cx]:
                break
        else:
            count += 1

    return count


def is_x_mas(x: int, y: int, input: list[str]) -> bool:
    if x == 0 or x == len(input[0]) - 1 or y == 0 or y == len(input) - 1:
        return False

    for d1, d2 in [((1, 1), (-1, -1)), ((1, -1), (-1, 1))]:
        d1x, d1y = d1
        d2x, d2y = d2

        concat = f'{input[y + d1y][x + d1x]}{input[y + d2y][x + d2x]}'

        if concat not in ('SM', 'MS'):
            return False

    return True


def part1(input: list[str]) -> int:
    count = 0

    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == 'X':
                count += count_word(x, y, 'XMAS', input)

    return count


def part2(input: list[str]) -> int:
    count = 0

    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == 'A' and is_x_mas(x, y, input):
                count += 1

    return count


test_input_1 = get_input('Day04_test_1')
input = get_input('Day04')

output_part1_test = part1(test_input_1)
assert output_part1_test == 18, f'{output_part1_test}'

output_part1 = part1(input)
assert output_part1 == 2549, f'{output_part1}'
print(output_part1)


test_input_2 = get_input('Day04_test_2')

output_part2_test = part2(test_input_2)
assert output_part2_test == 9, f'{output_part2_test}'

output_part2 = part2(input)
assert output_part2 == 2003, f'{output_part2}'
print(output_part2)
