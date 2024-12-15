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


def part1(input: list[str]) -> int:
    count = 0
    for y, line in enumerate(input):
        for x, c in enumerate(line):
            if c == 'X':
                count += count_word(x, y, 'XMAS', input)

    return count


with open('Day04_test.txt', 'r') as file:
    test_input = file.readlines()

with open('Day04.txt', 'r') as file:
    input = file.readlines()

output_part1_test = part1(test_input)
assert output_part1_test == 18, f'{output_part1_test}'

output_part1 = part1(input)
print(output_part1)
