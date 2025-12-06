from utils import time_solver, get_input


@time_solver
def part_one(data):
    result = 0
    index = 0
    fresh = []
    while data[index] != "": 
        fresh.append(list(map(int, data[index].split("-"))))
        index +=1
    while index +1 < len(data):
        index +=1
        for fr in fresh:
            if fr[0] <= int(data[index]) <= fr[1]:
                result += 1
                break
    return result


@time_solver
def part_two(data):
    result = 0
    return result



