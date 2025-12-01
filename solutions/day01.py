from utils import time_solver, get_input 

start = 50


@time_solver # Use the timing decorator
def part_one(data):
    count = 0
    current = start
    for i in range(len(data)):
        dir = data[i][0]
        number = int(data[i][1:])
        if dir == 'L':
            current += number
        else:
            current -= number
        if current % 100 == 0:
            count += 1
    return count

@time_solver
def part_two(data):
    # ... your solution logic
    return 1337


