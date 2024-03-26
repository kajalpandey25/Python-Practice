import os
folders = os.listdir("data")

print(folders)

print(os.getcwd())
os.chdir("/Users")

for folder in folders:
    print(os.listdir(f"data/{folder}"))
    print(folder)