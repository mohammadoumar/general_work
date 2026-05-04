import os

cwd = os.getcwd()
current_dir = cwd.split("\\")[-1]

print("Current directory: " + current_dir)