import os
import re

def format_filename(filename):
    # Define regex patterns to capture the number, difficulty, and title
    patterns = [
        r"(\d+)_([a-zA-Z]+)_(.+)\.py",  # 1123_medium_title_of_the_problem.py
        r"([a-zA-Z]+)_(\d+)_(.+)\.py",  # medium_124_Title_Of_the_problem.py
    ]
    
    for pattern in patterns:
        match = re.match(pattern, filename)
        if match:
            groups = list(match.groups())
            
            # Keep the problem number as-is
            number = groups[0] if groups[0].isdigit() else groups[1]
            difficulty = groups[1] if groups[0].isdigit() else groups[0]
            
            # Normalize title (replace spaces with underscores, lowercase everything)
            title = groups[2].replace(' ', '_').lower()
            
            # Build new filename
            new_filename = f"{number}_{difficulty}_{title}.py"
            return new_filename

    return None

def rename_files_in_directory(directory):
    for filename in os.listdir(directory):
        if filename.endswith('.py'):
            new_filename = format_filename(filename)
            if new_filename:
                old_path = os.path.join(directory, filename)
                new_path = os.path.join(directory, new_filename)
                os.rename(old_path, new_path)
                print(f"Renamed: {filename} -> {new_filename}")

# Usage
directory = './'  # Replace this with the path to your directory
rename_files_in_directory(directory)
