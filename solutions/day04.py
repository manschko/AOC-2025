from utils import time_solver, get_input


@time_solver
def part_one(data):
    result = 0
    for i, shelf in enumerate(data):
        for j, item in enumerate(shelf):
            if item == '@':
                srounding = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        x = j + dx 
                        y = i + dy
                        if 0 <= y < len(data) and 0 <= x < len(shelf):
                            if data[y][x] == '@':
                                srounding += 1
                if srounding < 4:
                    result += 1
    return result


@time_solver
def part_two(data):
    result = 0
    removed_rolles, shelfs = remove_rolls(data)
    result += removed_rolles
    while removed_rolles > 0:
        removed_rolles, shelfs = remove_rolls(shelfs)
        result += removed_rolles
    return result

def remove_rolls(shelfs):
    result = 0
    new_shelfs = shelfs.copy()
    for i, shelf in enumerate(shelfs):
        for j, item in enumerate(shelf):
            if item == '@':
                srounding = 0
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if dx == 0 and dy == 0:
                            continue
                        x = j + dx 
                        y = i + dy
                        if 0 <= y < len(shelfs) and 0 <= x < len(shelf):
                            if shelfs[y][x] == '@':
                                srounding += 1
                if srounding < 4:
                    new_shelfs[i] = new_shelfs[i][:j] + "." + new_shelfs[i][j+1:]
                    result += 1
    return result, new_shelfs

