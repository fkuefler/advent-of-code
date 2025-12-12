import os

file_path = os.path.join(os.path.dirname(__file__), "input_day_3.txt")
with open(file_path, "r") as file:
    input_ = file.read()

BATTERY_LENGTHS = {2, 12}
total = 0

for bat_len in BATTERY_LENGTHS:
    for line in input_.split("\n"):
        digits = [0] * bat_len
        for i in range(len(line)):
            for d in range(max(i - len(line) + bat_len, 0), bat_len):
                if int(line[i]) > digits[d]:
                    digits[d] = int(line[i])
                    digits[d + 1 : bat_len] = [0] * (bat_len - d - 1)
                    break
        total += int("".join(map(str, digits)))
    print(f"Total joltage for batteries of length {bat_len}:", total)
    total = 0
