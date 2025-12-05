from utils import time_solver, get_input

INPUT_CONFIG = {
    'split_by': ',',  # or ',' or '\n\n' or None for raw text
    'strip': True
}


# possible solutions: len(item) /2  10 % 11 1000 % 101 100000 % 1001 = pow(10, len(item) +1) //2) 
@time_solver
def part_one(data):
    result = 0
    r2 = []
    for item in data:
        parts = item.split('-')
        parts[0] = int(parts[0])
        parts[1] = int(parts[1])
        l = len(str(parts[0]))
        multi = 10 ** (l // 2) + 1
        while parts[0] <= parts[1]:
            l = len(str(parts[0]))
            if l % 2 == 0:
                if parts[0] % multi == 0:
                    result += parts[0]
                    r2.append(parts[0])
                    parts[0] += multi
                else:
                    parts[0] = (parts[0] // multi + 1) * multi

            else:
                parts[0] = 10 ** (l) + 10 ** (l // 2)
                multi = 10 ** ((l + 1) // 2) + 1

    return result


@time_solver
def part_two(data):
    result = 0
    for item in data:
        parts = item.split('-')
        parts[0] = int(parts[0])
        parts[1] = int(parts[1])
        for r in range(parts[0], parts[1] + 1):
            if number_check(r):
                result += r
    return result


def number_check(num):
    numberStr = str(num)
    div = 2
    while div <= len(numberStr):
        if len(numberStr) % div != 0:
            div += 1
            continue

        part_size = len(numberStr) // div
        parts = []
        for i in range(div):
            start_index = i * part_size
            end_index = (i + 1) * part_size
            part = numberStr[start_index:end_index]
            parts.append(part)
        if all(digit == parts[0] for digit in parts):
            return True
        div += 1
    return False


