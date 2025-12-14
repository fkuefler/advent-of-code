import os

file_path = os.path.join(os.path.dirname(__file__), "input_day_5.txt")
with open(file_path, "r") as file:
    input_ = file.read()

ranges = []

for line in input_.split("\n"):
    if line.count("-"):
        ranges.append((int(line.split("-")[0]), int(line.split("-")[1])))

p1_total = 0

for line in input_.split("\n"):
    if not line.count("-") and len(line) > 0:
        for start, end in ranges:
            if int(line) >= start and int(line) <= end:
                p1_total += 1
                break

print("Part 1 Answer:", p1_total)

p2_total = 0
ranges = sorted(ranges)

last_end = -1
for start, end in ranges:
    if end <= last_end:
        continue
    p2_total += end - last_end if start <= last_end else end - start + 1
    last_end = end

print("Part 2 Answer:", p2_total)
