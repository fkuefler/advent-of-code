import math
import os

file_path = os.path.join(os.path.dirname(__file__), "input_day_6.txt")
with open(file_path, "r") as file:
    input_ = file.read()

# Part 1

terms = [[term.strip() for term in chunk.split()] for chunk in input_.split("\n")]
total = 0

for i in range(len(terms[0])):
    if terms[4][i] == "+":
        total += (
            int(terms[0][i]) + int(terms[1][i]) + int(terms[2][i]) + int(terms[3][i])
        )
    else:
        total += (
            int(terms[0][i]) * int(terms[1][i]) * int(terms[2][i]) * int(terms[3][i])
        )

print("Part 1 Answer: ", total)

# Part 2

terms2 = input_.split("\n")
total2 = 0

numbers = []
number = count = 0

for j in range(len(terms2[0]) - 1, -1, -1):
    for i in range(3, -1, -1):
        if terms2[i][j] != " ":
            number += int(terms2[i][j]) * (10**count)
            count += 1
    numbers.append(number) if number != 0 else None
    if terms2[4][j] == "*":
        total2 += math.prod(numbers)
        numbers.clear()
    elif terms2[4][j] == "+":
        total2 += sum(numbers)
        numbers.clear()
    number = count = 0

print("Part 2 Answer: ", total2)
