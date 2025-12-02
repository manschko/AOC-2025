import os
import sys
import importlib
from utils import get_input

def get_available_days():
    """Scan solutions directory for available day solutions."""
    solutions_dir = 'solutions'
    days = []
    for filename in os.listdir(solutions_dir):
        if filename.startswith('day') and filename.endswith('.py'):
            day_num = filename[3:5]
            if day_num.isdigit():
                days.append(int(day_num))
    return sorted(days)

def main():
    print("=" * 50)
    print("  Advent of Code 2025 - Solution Runner")
    print("=" * 50)
    
    # Get available days
    available_days = get_available_days()
    
    if not available_days:
        print("No solution files found in the solutions directory.")
        sys.exit(1)
    
    print(f"\nAvailable days: {', '.join(map(str, available_days))}")
    
    # Get day selection
    newest_day = max(available_days)
    while True:
        try:
            day_input = input(f"\nEnter day number (1-25) [default: {newest_day}]: ").strip()
            if not day_input:
                day = newest_day
                break
            day = int(day_input)
            if day not in available_days:
                print(f"Day {day} not available. Please choose from: {available_days}")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
        except KeyboardInterrupt:
            print("\nExiting...")
            sys.exit(0)
    
    # Get input type selection
    while True:
        choice = input("Use example input? (y/n) [default: y]: ").strip().lower()
        if not choice:
            is_example = True
            break
        elif choice in ['y', 'yes']:
            is_example = True
            break
        elif choice in ['n', 'no']:
            is_example = False
            break
        else:
            print("Please enter 'y' or 'n'.")
    
    # Import solution module
    try:
        day_module = importlib.import_module(f'solutions.day{str(day).zfill(2)}')
    except ModuleNotFoundError:
        print(f"Error: Solution file for Day {day} not found.")
        sys.exit(1)
    
    # Get input data
    input_data = get_input(day, is_example)
    if not input_data:
        sys.exit(1)
    
    print(f"\n{'=' * 50}")
    print(f"  Running Day {day} (Example: {is_example})")
    print(f"{'=' * 50}\n")
    
    # Run solutions
    day_module.part_one(input_data)
    day_module.part_two(input_data)
    
    print(f"\n{'=' * 50}")
    print("  Completed!")
    print(f"{'=' * 50}\n")

if __name__ == "__main__":
    main()
