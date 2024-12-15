def get_input(filename: str) -> list[str]:
    with open(f'{filename}.txt', 'r') as file:
        lines = file.readlines()

    return lines
