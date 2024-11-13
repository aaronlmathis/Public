import os

def rename_files_in_directory(directory):
    python_dir = os.path.join(directory, 'python')
    go_dir = os.path.join(directory, 'go')

    # Ensure target directories exist
    os.makedirs(python_dir, exist_ok=True)
    os.makedirs(go_dir, exist_ok=True)

    for filename in os.listdir(directory):
        old_path = os.path.join(directory, filename)

        if filename.endswith('.py'):
            new_path = os.path.join(python_dir, filename)
            os.rename(old_path, new_path)
            print(f"Moved: {old_path} -> {new_path}")

        elif filename.endswith('.go'):
            new_path = os.path.join(go_dir, filename)
            os.rename(old_path, new_path)
            print(f"Moved: {old_path} -> {new_path}")

# Usage
directory = './'  # Replace this with the path to your directory
rename_files_in_directory(directory)