import sys
import importlib
from utils import get_input # Import the utility function

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python run.py <day_number> [example]")
        sys.exit(1)

    day = int(sys.argv[1])
    is_example = len(sys.argv) > 2 and sys.argv[2] == 'example'

    # Dynamically import the solution file for the specified day
    try:
        day_module = importlib.import_module(f'solutions.day{str(day).zfill(2)}')
    except ModuleNotFoundError:
        print(f"Error: Solution file for Day {day} not found.")
        sys.exit(1)
        
    # 1. Get Input
    input_data = get_input(day, is_example)
    if not input_data:
        sys.exit(1)

    print(f"\n--- Running Day {day} (Example: {is_example}) ---")
    
    # 2. Run and Time Part 1
    # The @time_solver decorator (if used) will handle timing and printing
    day_module.part_one(input_data)
    
    # 3. Run and Time Part 2
    day_module.part_two(input_data)