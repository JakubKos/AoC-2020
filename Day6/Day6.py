

def part1(input_filepath: str):
    result = 0
    answer = ''

    with open(input_filepath, 'r') as file:
        for line in file:
            if line == '\n':
                result += len(answer)
                answer = ""
                continue

            for letter in line.strip().replace(' ', ''):
                if letter not in answer:
                    answer += letter
    result += len(answer)
    return result


def process_letter(letter: str, answers: list):
    for answer in answers:
        if letter not in answer:
            return False
    return True


def decode_answers(answers: list):
    result = 0
    for letter in answers[0]:
        if process_letter(letter, answers):
            result += 1
    return result


def part2(input_filepath: str):
    result = 0
    individual_answers = []
    answer = ''

    with open(input_filepath, 'r') as file:
        for line in file:
            if line == '\n':
                result += decode_answers(individual_answers)
                individual_answers = []
                continue

            for letter in line.strip().replace(' ', ''):
                if letter not in answer:
                    answer += letter

            individual_answers.append(answer)
            answer = ''
    result += decode_answers(individual_answers)
    return result


if __name__ == '__main__':
    print(part1("input"))
    print(part2("input"))
