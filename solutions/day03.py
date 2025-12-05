from utils import time_solver, get_input


# possible solutions: len(item) /2  10 % 11 1000 % 101 100000 % 1001 = pow(10, len(item) +1) //2) 
@time_solver
def part_one(data):
    result = 0
    for bank in data:
        highest = 0
        s_highest = 0
        last_index = len(bank) - 1
        for inex, bat in enumerate(bank):
            battery = int(bat)
            if battery > highest and inex != last_index:
                s_highest = 0
                highest = battery
            elif battery > s_highest:
                s_highest = battery

        result += highest * 10 + s_highest
    return result


@time_solver
def part_two(data):
    result = 0
    return result

