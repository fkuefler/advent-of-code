import os

file_path = os.path.join(os.path.dirname(__file__), "input_day_4.txt")
with open(file_path, "r") as file:
    input_ = file.read().split("\n")


# Counts the number of adjacent '@'
def count_adjs(i: int, j: int) -> int:
    count = 0
    for k in [-1, 0, 1]:
        for l in [-1, 0, 1]:
            if (
                k == l == 0
                or i + k < 0
                or i + k >= len(input_)
                or j + l < 0
                or j + l >= len(input_[0])
            ):
                continue
            count += 1 if input_[i + k][j + l] == "@" else 0
    return count


# Part 1

p1_total = 0
for i in range(len(input_)):
    for j in range(len(input_[0])):
        if count_adjs(i, j) < 4 and input_[i][j] == "@":
            p1_total += 1

print("Part 1 Answer: ", p1_total)

p2_total = 0
i = j = 0

# Part 2

while i < len(input_):
    while j < len(input_[0]):
        if input_[i][j] == "@" and count_adjs(i, j) < 4:
            p2_total += 1
            input_[i] = input_[i][:j] + "." + input_[i][j + 1 :]
            i = max(0, i - 1)
            j = max(0, j - 1)
            break
        else:
            j += 1
    if j == len(input_[0]):
        j = 0
        i += 1

print("Part 2 Answer: ", p2_total)
