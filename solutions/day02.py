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
        multi = 10**(l // 2) +1
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
                parts[0] = 10**(l) +  10**(l // 2)
                multi = 10**((l + 1) // 2) +1
        
        

    return result

@time_solver
def part_two(data):
    return data

