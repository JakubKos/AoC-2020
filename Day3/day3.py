

def tree_traverse(input_filepath: str, right_shift: int, down_shift: int):
    tree_count = 0
    current_position = 0
    down_skip = 0

    with open(input_filepath, 'r') as file:
        next(file)
        for line in file:
            down_skip += 1
            if down_skip % down_shift != 0:
                continue

            current_position += right_shift
            if line.strip()[current_position % len(line.strip())] == '#':
                tree_count += 1

    return tree_count


def part1(input_filepath: str):
    return tree_traverse(input_filepath, 3, 1)


def part2(input_filepath: str):
    return (tree_traverse(input_filepath, 1, 1) *
            tree_traverse(input_filepath, 3, 1) *
            tree_traverse(input_filepath, 5, 1) *
            tree_traverse(input_filepath, 7, 1) *
            tree_traverse(input_filepath, 1, 2))


if __name__ == '__main__':
    print(part1("input"))
    print(part2("input"))
