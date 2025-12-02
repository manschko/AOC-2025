import os

def get_input(day_number, is_example=False, split_by='\n', strip=True):
    """Reads the input file for a given day."""
    # ... (rest of the input reading code)
    file_prefix = 'day' + str(day_number).zfill(2)
    file_suffix = '_ex' if is_example else ''
    file_path = os.path.join('inputs', f'{file_prefix}{file_suffix}.txt')
    
    try:
        with open(file_path, 'r') as f:
            content = f.read()
            
            if split_by is None:
                return content
            elif split_by == '\n':
                result = content.splitlines()
            else:
                result = content.split(split_by)
            
            if strip:
                result = [item.strip() for item in result]
            
            return result
    except FileNotFoundError:
        print(f"Error: Input file not found at {file_path}")
        return [] if split_by is not None else ""