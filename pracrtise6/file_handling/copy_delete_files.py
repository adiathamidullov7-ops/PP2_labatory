import os
import shutil

with open("sample.txt", "a") as file:
    file.write("Line 4: It was Appended text\n")

print("Text appended")

shutil.copy("sample.txt", "backup_sample.txt")
print("File copied as backup_sample.txt")

if os.path.exists("backup_sample.txt"):
    os.remove("backup_sample.txt")
    print("Backup file deleted")