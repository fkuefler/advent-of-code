#include <array>
#include <fstream>
#include <iostream>
#include <vector>

int main() {
  std::ifstream file("input_day_3.txt");
  if (!file.is_open()) {
    std::cerr << "Failed to open input" << std::endl;
    return 1;
  }

  std::vector<std::string> lines;
  std::string line;
  while (std::getline(file, line)) {
    if (line.back() == '\r') line.pop_back();
    lines.push_back(line);
  }

  for (auto bat_len : {2, 12}) {
    unsigned long total = 0;
    for (const auto& line : lines) {
      unsigned long joltage = 0;
      std::vector<int> digits(bat_len, 0);
      for (int i = 0; i < line.size(); i++) {
        for (int d = std::max(i - static_cast<int>(line.size()) + bat_len, 0);
             d < bat_len; d++) {
          if (line[i] - '0' > digits[d]) {
            digits[d] = line[i] - '0';
            for (int j = d + 1; j < bat_len; j++) digits[j] = 0;
            break;
          }
        }
      }
      for (auto d : digits) {
        joltage = joltage * 10 + d;
      }
      total += joltage;
    }
    std::cout << "Total joltage for batteries of length " << bat_len << ": "
              << total << '\n';
  }
}