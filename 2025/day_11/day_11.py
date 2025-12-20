import os
from collections import defaultdict
from functools import lru_cache


file_path = os.path.join(os.path.dirname(__file__), "input_day_11.txt")
with open(file_path, "r") as file:
    input_ = file.read()

adjs = defaultdict(list)
for line in input_.split("\n"):
    adjs[line[:3]] = line[4:].split()


def count_paths(start: str, end: str):
    @lru_cache(None)
    def dfs(x):
        if x == end:
            return 1
        paths = 0
        for y in adjs[x]:
            paths += dfs(y)
        return paths

    return dfs(start)


print("Part 1 Answer:", count_paths("you", "out"))
print(
    "Part 2 Answer:",
    count_paths("svr", "dac") * count_paths("dac", "fft") * count_paths("fft", "out")
    + count_paths("svr", "fft") * count_paths("fft", "dac") * count_paths("dac", "out"),
)
