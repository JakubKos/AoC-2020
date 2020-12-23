import string


def acquire_passports(input_filepath: str):
    passports_list = []
    passport = {}

    with open(input_filepath, 'r') as file:
        for line in file:
            if line != '\n':
                characteristics = line.split(' ')
                for characteristic in characteristics:
                    key, value = characteristic.split(':')
                    passport[key.strip()] = value.strip()
                continue

            passports_list.append(passport)
            passport = {}
    passports_list.append(passport)

    return passports_list


def check_valid_passport(passport: dict):
    for characteristic in ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]:
        if characteristic not in passport.keys():
            return False
    return True


def check_passport_values(passport: dict):
    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        return False

    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        return False

    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        return False

    if passport['hgt'][-2:] == 'cm':
        if int(passport['hgt'][:-2]) < 150 or int(passport['hgt'][:-2]) > 193:
            return False
    elif passport['hgt'][-2:] == 'in':
        if int(passport['hgt'][:-2]) < 59 or int(passport['hgt'][:-2]) > 76:
            return False
    else:
        return False

    hair_color = passport['hcl']
    if not (hair_color.startswith('#') and
            len(hair_color) == 7 and
            all(character in string.hexdigits for character in hair_color[1:])):
        return False

    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False

    if len(passport['pid']) != 9 or any(character not in string.digits for character in passport['pid']):
        return False

    return True


def part1(input_filepath: str):
    valid_passports = 0
    for passport in acquire_passports(input_filepath):
        if check_valid_passport(passport):
            valid_passports += 1

    return valid_passports


def part2(input_filepath: str):
    valid_passports = 0
    for passport in acquire_passports(input_filepath):
        if check_valid_passport(passport) and check_passport_values(passport):
            valid_passports += 1

    return valid_passports


if __name__ == '__main__':
    print(part1("input"))
    print(part2("input"))
