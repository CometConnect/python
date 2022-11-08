import shutil
import os

try:
    shutil.move(
        os.path.join(os.getcwd(), "Downloads", "l.txt"),
        os.path.join(os.getcwd(), "Data")
    )
except shutil.Error:
    print("Same file already exists")
