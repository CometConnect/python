import os
import shutil

# change these according to your needs
f1 = "Downloads"  # target
f2 = "Data"  # destination

folder1_path = os.path.join(os.getcwd(), f1)
folder2_path = os.path.join(os.getcwd(), f2)

if not os.path.exists(folder1_path):
    print(f"{f1} doesn't exist")
    exit(1)
if not os.path.exists(folder2_path):
    print(f"{f2} doesn't exist")
    exit(1)


def check_or_make(path):
    full_path = os.path.join(folder2_path, path)
    if not os.path.exists(full_path):  # check if path exists, if not make it
        os.mkdir(full_path)

    if not os.path.isdir(full_path):  # make sure it's a directory
        os.mkdir(full_path)

    return full_path


file_list = os.listdir(folder1_path)
extension_to_dir = {
    ".accdb": "Access Databases",
    ".xlsx": "Excel Worksheets",
    ".pptx": "Powerpoint Presentations",
    ".pub": "Publisher Documents",
    ".docx": "Word Documents"
}
for file in file_list:
    [_, extension] = os.path.splitext(os.path.join(folder1_path, file))
    folder_path = check_or_make(extension_to_dir[extension])
    shutil.move(
        os.path.join(folder1_path, file),
        folder_path
    )

    print(f"{os.path.join(f1, file)} -> {os.path.join(folder_path, file)}")
