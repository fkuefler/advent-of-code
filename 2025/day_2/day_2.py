import os

file_path = os.path.join(os.path.dirname(__file__), "input_day_2.txt")
with open(file_path, "r") as file:
    input_ = file.read()

p1_total = 0
p2_total = 0
seen = set()

for range_ in input_.split(","):
    for i in range(int(range_.split("-")[0]), int(range_.split("-")[1]) + 1):
        for l in range(1, (len(str(i)) // 2) + 1):
            if len(str(i)) % l == 0:
                chunks = [str(i)[k : k + l] for k in range(0, len(str(i)), l)]
                if all(chunk == chunks[0] for chunk in chunks) and i not in seen:
                    if len(chunks) == 2:
                        p1_total += i
                    p2_total += i
                    seen.add(i)


print("Part 1 Answer: ", p1_total)
print("Part 2 Answer: ", p2_total)
