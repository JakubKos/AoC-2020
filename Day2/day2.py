
def parse_policy(policy: str):
    restriction, letter, password = policy.strip().split(' ')
    restriction_low, restriction_high = restriction.split('-')
    restriction_low, restriction_high = int(restriction_low), int(restriction_high)
    letter = letter[:-1]
    return restriction_low, restriction_high, letter, password


def solve_part(input_filepath: str, part: bool):
    """
    :param part: true if part1, false otherwise
    """
    valid_passwords = 0

    with open(input_filepath, 'r') as file:
        for line in file:
            restriction_low, restriction_high, letter, password = parse_policy(line)

            if part and restriction_low <= password.count(letter) <= restriction_high:
                valid_passwords += 1
            if not part and (password[restriction_low - 1] == letter) != (password[restriction_high - 1] == letter):
                valid_passwords += 1
    return valid_passwords


def part1(input_filepath: str):
    return solve_part(input_filepath, True)


def part2(input_filepath: str):
    return solve_part(input_filepath, False)


if __name__ == '__main__':
    print(part1("input"))
    print(part2("input"))
