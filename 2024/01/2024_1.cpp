#include <iostream>
#include <set>
#include <vector>
using namespace std;

int main(int argc, char **argv) {
  FILE *f = fopen("1.in", "r");
  int a, b;
  vector<int> l1, l2;
  while (fscanf(f, "%d %d\n", &a, &b) == 2) {
    l1.push_back(a);
    l2.push_back(b);
  }
  fclose(f);
  sort(l1.begin(), l1.end());
  sort(l2.begin(), l2.end());
  int s = 0;
  for (int i = 0; i < l1.size(); i++) {
    s += abs(l1[i] - l2[i]);
  }
  cout << "p1: " << s << "\n";

  multiset<int> ms(l2.begin(), l2.end());
  int sum2 = 0;
  for (int x : l1) {
    sum2 += x * ms.count(x);
  }
  cout << "p2: " << sum2 << "\n";
}
