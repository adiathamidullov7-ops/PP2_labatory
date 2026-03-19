import shutil
import os

os.makedirs("storage", exist_ok=True)
if os.path.exists("sample.txt"):
    shutil.move("sample.txt", "storage/sample.txt")
    print("File moved to storage folder")

shutil.copy("storage/sample.txt", "storage/sample_copy.txt")
print("File copied inside storage")
