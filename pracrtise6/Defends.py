import os
from functools import reduce


folder = "scores"
os.makedirs(folder, exist_ok=True)


file_path = os.path.join(folder, "class1.txt")

with open(file_path, "w", encoding="utf-8") as f:
    f.write("Alice,85\n")
    f.write("Bob,90\n")
    f.write("Charlie,78\n")
    f.write("David,92\n")
    f.write("Eve,88\n")

print("Файл создан!\n")

#  Read files
students = []

for filename in os.listdir(folder):
    if filename.endswith(".txt"):
        path = os.path.join(folder, filename)

        with open(path, "r", encoding="utf-8") as f:
            for line in f:
                name, score = line.strip().split(",")
                students.append((name, int(score)))

# All information
names = [s[0] for s in students]
scores = [s[1] for s in students]



# 1. All students
print("All students:", len(students))

# 2. Total scores
print("Total scores:", sum(scores))

# 3. Max and Min
print("MAX SCORES:", max(scores))
print("Min scores:", min(scores))

# 4. +5 scores
new_scores = list(map(lambda x: x + 5, scores))
print("After +5:", new_scores)

# 5. Students > 85
top_students = list(filter(lambda x: x[1] > 85, students))
print("\nGreat students:")

for s in top_students:
    print(s)

# Work
product = reduce(lambda x, y: x * y, scores)
print("\nAll scores:", product)

#  enumerate
print("\nAll Students:")
for i, (name, score) in enumerate(students, start=1):
    print(i, name, score)

#  zip
combined = list(zip(names, scores))
print("\nZip:", combined)

#  Sorting
sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
print("\nSORTING:")
for s in sorted_students:
    print(s)


with open("report.txt", "w", encoding="utf-8") as r:
    r.write(f"Total students: {len(students)}\n")
    r.write(f"Average score: {sum(scores)/len(scores):.2f}\n")
    r.write(f"Highest score: {max(scores)}\n")
    r.write(f"Lowest score: {min(scores)}\n")
    r.write("Top students:\n")

    for name, score in top_students:
        r.write(f"{name} {score}\n")

print("\nFile was created on report.txt")