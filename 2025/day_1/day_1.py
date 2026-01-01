import os

file_path = os.path.join(os.path.dirname(__file__), "input_day_1.txt")
with open(file_path, "r") as file:
    input_ = file.read()

pos = 50
p1_count = p2_count = 0

for line in input_.split("\n"):
    if line[0] == "L":
        p2_count += abs((pos - int(line[1:])) // 100) - int(pos == 0)
        pos = (pos - int(line[1:])) % 100
        if pos == 0:
            p1_count += 1
            p2_count += 1
    else:
        p2_count += abs((pos + int(line[1:])) // 100)
        pos = (pos + int(line[1:])) % 100
        if pos == 0:
            p1_count += 1

print("Part 1 Answer: ", p1_count)
print("Part 2 Answer: ", p2_count)
