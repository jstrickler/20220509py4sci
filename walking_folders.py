import os

start_dir = "."

for folder, subfolders, files in os.walk(start_dir):
    if '.git' in subfolders:
        subfolders.remove('.git')
    print(folder)
    for file_name in files:
        if file_name.endswith('.txt'):
            file_path = os.path.join(folder, file_name)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:8d} {file_name}")

