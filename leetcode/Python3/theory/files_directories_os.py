import os
import glob
import shutil

# 1️⃣ LISTING FILES & DIRECTORIES

# List all files & folders in a directory
files = os.listdir('/path/to/directory')
print(files)

# More efficient directory listing
with os.scandir('/path/to/directory') as entries:
    for entry in entries:
        print(entry.name, entry.is_file(), entry.is_dir())

# Get specific files using glob
csv_files = glob.glob('/path/to/directory/*.csv')
print(csv_files)

# Recursive listing of files & subdirectories
for root, dirs, files in os.walk('/path/to/directory'):
    print(f"Directory: {root}")
    for file in files:
        print(f"  File: {file}")

# 2️⃣ MODIFYING FILE NAMES

# Rename a single file
os.rename("old_file.txt", "new_file.txt")

# Rename multiple files in a directory
directory = "/path/to/directory"
for filename in os.listdir(directory):
    if filename.endswith(".txt"):
        old_path = os.path.join(directory, filename)
        new_path = os.path.join(directory, f"new_{filename}")
        os.rename(old_path, new_path)

# Change file extensions
for filename in os.listdir('.'):
    if filename.endswith('.txt'):
        new_filename = filename.replace('.txt', '.md')
        os.rename(filename, new_filename)

# 3️⃣ READING & WRITING FILES

# Read an entire file
with open("file.txt", "r") as f:
    content = f.read()
    print(content)

# Read a file line by line
with open("file.txt", "r") as f:
    for line in f:
        print(line.strip())

# Write to a file (overwrite)
with open("file.txt", "w") as f:
    f.write("Hello, World!\n")

# Append to a file
with open("file.txt", "a") as f:
    f.write("Appending new line.\n")

# Read & Write within the same file
with open("file.txt", "r+") as f:
    content = f.read()
    f.write("\nThis is new content added at the end.")

# Writing multiple lines
lines = ["Line 1\n", "Line 2\n", "Line 3\n"]
with open("file.txt", "w") as f:
    f.writelines(lines)

# 4️⃣ COPYING & MOVING FILES

# Copy a file
shutil.copy("file.txt", "backup_file.txt")

# Move a file
shutil.move("file.txt", "/new/path/file.txt")

# 5️⃣ DELETING FILES & DIRECTORIES

# Delete a file
if os.path.exists("file.txt"):
    os.remove("file.txt")

# Delete an empty directory
os.rmdir("empty_directory")

# Delete a directory with files
shutil.rmtree("directory_with_files")

# 6️⃣ WORKING WITH FILE PATHS

# Get absolute path
file_path = os.path.abspath("file.txt")
print(file_path)

# Get filename & extension
file = "/path/to/file.txt"
print(os.path.basename(file))  # file.txt
print(os.path.splitext(file))  # ('/path/to/file', '.txt')

# Check if a file exists
if os.path.isfile("file.txt"):
    print("File exists")

# Check if a directory exists
if os.path.isdir("my_directory"):
    print("Directory exists")

# Create a directory (if not exists)
os.makedirs("new_directory", exist_ok=True)

# 7️⃣ SEARCHING FOR FILES

# Find a specific file
for root, dirs, files in os.walk("/path/to/directory"):
    for file in files:
        if file == "target_file.txt":
            print(os.path.join(root, file))

# Find all files with a specific extension
for root, dirs, files in os.walk("/path/to/directory"):
    for file in files:
        if file.endswith(".csv"):
            print(os.path.join(root, file))

# Search for files containing a keyword in the name
search_term = "invoice"
for root, dirs, files in os.walk("/path/to/directory"):
    for file in files:
        if search_term in file:
            print(os.path.join(root, file))
