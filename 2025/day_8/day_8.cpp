#include <algorithm>
#include <fstream>
#include <iostream>
#include <string>
#include <vector>

class DSU {
 private:
  std::vector<int> parent;

 public:
  std::vector<int> sizes;
  int max_size = 1;

  DSU(int n) {
    parent = std::vector<int>(n);
    for (int i = 0; i < parent.size(); i++) parent[i] = i;
    sizes = std::vector<int>(n, 1);
  }

  int find(int i) {
    if (parent[i] == i) return i;
    parent[i] = find(parent[i]);
    return parent[i];
  }

  void merge(int i, int j) {
    int i_rep = find(i);
    int j_rep = find(j);
    if (i_rep != j_rep) {
      parent[i_rep] = j_rep;
      sizes[j_rep] += sizes[i_rep];
      sizes[i_rep] = 1;
      max_size = std::max(max_size, sizes[j_rep]);
    }
  }
};

struct Coord {
  int x, y, z;
};

struct Edge {
  int i, j;
  long long length;

  Edge(int i_, int j_, const std::vector<Coord>& coords) : i(i_), j(j_) {
    const auto& a = coords[i];
    const auto& b = coords[j];
    length = 1LL * (a.x - b.x) * (a.x - b.x) + 1LL * (a.y - b.y) * (a.y - b.y) +
             1LL * (a.z - b.z) * (a.z - b.z);
  }
};

int main() {
  std::ifstream file("input_day_8.txt");
  if (!file.is_open()) {
    std::cerr << "Failed to open input\n";
    return 1;
  }

  std::vector<Coord> coords;
  int a, b, c;
  char ignore;

  while (file >> a >> ignore >> b >> ignore >> c) {
    coords.emplace_back(Coord{a, b, c});
  }

  std::vector<Edge> edges;
  edges.reserve(coords.size() * (coords.size() - 1) / 2);

  for (int i = 0; i < coords.size(); i++) {
    for (int j = i + 1; j < coords.size(); j++) {
      edges.emplace_back(Edge(i, j, coords));
    }
  }

  std::sort(edges.begin(), edges.end(),
            [](const auto& a, const auto& b) { return a.length < b.length; });

  DSU dsu = DSU(coords.size());

  for (int k = 0; k < edges.size(); k++) {
    dsu.merge(edges[k].i, edges[k].j);
    if (k == 999) {
      int a = 0, b = 0, c = 0;
      for (int x : dsu.sizes) {
        if (x > a) {
          c = b;
          b = a;
          a = x;
        } else if (x > b) {
          c = b;
          b = x;
        } else if (x > c) {
          c = x;
        }
      }
      std::cout << "Part 1 Answer: " << a * b * c << "\n";
    }
    if (dsu.max_size == coords.size()) {
      std::cout << "Part 2 Answer: "
                << 1LL * coords[edges[k].i].x * coords[edges[k].j].x << "\n";
      break;
    }
  }
}