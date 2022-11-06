import os
import shutil

f1 = input("Enter folder 1:")
f2 = input("Enter folder 2:")

folder1_path = os.path.join(os.getcwd(), f1)
folder2_path = os.path.join(os.getcwd(), f2)

if not os.path.exists(folder1_path):
    print("folder1 doesn't exist")
    exit(1)
if not os.path.exists(folder2_path):
    print("folder2 doesn't exit")
    exit(1)

file_list = os.listdir(folder1_path)
for file in file_list:
    shutil.move(
        os.path.join(os.getcwd(), f1, file),
        folder2_path
    )

print("Files moved")
