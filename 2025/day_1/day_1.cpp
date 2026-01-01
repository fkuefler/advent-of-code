#include <cmath>
#include <fstream>
#include <iostream>
#include <string>

int main() {
  std::ifstream file("input_day_1.txt");
  if (!file.is_open()) {
    std::cerr << "Failed to open input" << std::endl;
    return 1;
  }

  int p1_count, p2_count = 0;
  int pos = 50;

  char dir;
  int value;

  while (file >> dir >> value) {
    if (dir == 'L') {
      p2_count += std::abs(std::floor((pos - value) / 100.0)) - (pos == 0);
      pos = (((pos - value) % 100) + 100) % 100;
      if (pos == 0) {
        p1_count++;
        p2_count++;
      }
    } else {
      p2_count += std::abs(std::floor((pos + value) / 100.0));
      pos = (pos + value) % 100;
      if (pos == 0) p1_count++;
    }
  }

  std::cout << "Part 1 Answer: " << p1_count << std::endl;
  std::cout << "Part 2 Answer: " << p2_count << std::endl;

  return 0;
}