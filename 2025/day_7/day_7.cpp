#include <fstream>
#include <iostream>
#include <numeric>
#include <string>
#include <unordered_set>
#include <vector>

int main() {
  std::ifstream file("input_day_7.txt");
  if (!file.is_open()) {
    std::cerr << "Failed to open input\n";
    return 1;
  }

  std::vector<std::string> input_;
  std::string line;
  while (std::getline(file, line)) input_.push_back(line);

  auto start_pos = input_[0].find('S');

  std::unordered_set<int> beams;
  beams.insert(start_pos);
  int p1_count = 0;

  std::vector<long long> tls(input_[1].size(), 0);
  tls[start_pos] = 1;

  for (int r = 1; r < input_.size(); r++) {
    for (int c = 0; c < input_[r].size(); c++) {
      if (input_[r][c] == '^') {
        if (beams.count(c)) {
          p1_count++;
          beams.erase(c);
          beams.insert(c + 1);
          beams.insert(c - 1);
        }
        if (tls[c] != 0) {
          tls[c - 1] += tls[c];
          tls[c + 1] += tls[c];
          tls[c] = 0;
        }
      }
    }
  }

  std::cout << "Part 1 Answer: " << p1_count << "\n";
  auto p2_count = std::accumulate(tls.begin(), tls.end(), 0ULL);
  std::cout << "Part 2 Answer: " << p2_count << "\n";
}