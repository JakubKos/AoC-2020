import sys


def decode_position(seat: str, row: bool):
    """
    :param row: True if row is decoded, false otherwise(column)
    """
    low, high = (0, 127) if row else (0, 7)
    front_left, back_right = ('F', 'B') if row else ('L', 'R')

    for half in seat:
        if half == front_left:
            high = (low + high) // 2
        elif half == back_right:
            low = (low + high) // 2 + 1
    return low


def acquire_seats(input_filepath: str):
    seats = []
    with open(input_filepath, 'r') as file:
        for line in file:
            row = decode_position(line[0:7], True)
            column = decode_position(line[7:], False)
            seat_id = row * 8 + column
            seats.append((row, column, seat_id))
    return seats


def part1(input_filepath: str):
    highest_id = -sys.maxsize
    for _, _, seat_id in acquire_seats(input_filepath):
        if seat_id > highest_id:
            highest_id = seat_id

    return highest_id


def part2(input_filepath: str):
    seats = sorted(acquire_seats(input_filepath))
    expected_position = seats[0][2]

    for _, _, seat_id in seats:
        if expected_position != seat_id:
            return expected_position
        expected_position += 1
    return None


if __name__ == '__main__':
    print(part1("input"))
    print(part2("input"))
