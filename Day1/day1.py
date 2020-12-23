

def handle_input(input_filepath: str):
    expense_list = []

    with open(input_filepath, 'r') as file:
        for line in file:
            expense_list.append(int(line.strip()))
    return expense_list


def part1(input_filepath: str):
    expense_list = handle_input(input_filepath)

    for number in expense_list:
        for second_number in expense_list:
            if number + second_number == 2020:
                return number * second_number


def part2(input_filepath: str):
    expense_list = handle_input(input_filepath)

    for number in expense_list:
        for second_number in expense_list:
            for third_number in expense_list:
                if number + second_number + third_number == 2020:
                    return number * second_number * third_number


if __name__ == '__main__':
    print(part1("input"))
    print(part2("input"))
