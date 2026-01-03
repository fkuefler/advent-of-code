import os

file_path = os.path.join(os.path.dirname(__file__), "input_day_7.txt")
with open(file_path, "r") as file:
    input_ = file.read().split("\n")

beams = set()
beams.add(start_pos := input_[0].find("S"))
p1_count = 0

tls = [0] * len(input_[1])
tls[start_pos] = 1

for row in input_[1:]:
    for i in range(len(row)):
        if row[i] == "^":
            if i in beams:
                p1_count += 1
                beams.discard(i)
                beams.add(i + 1)
                beams.add(i - 1)
            if tls[i] != 0:
                tls[i - 1] += tls[i]
                tls[i + 1] += tls[i]
                tls[i] = 0

print("Part 1 Answer:", p1_count)
print("Part 2 Answer:", sum(tls))
