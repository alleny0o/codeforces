#include <iostream>
#include <map>
using namespace std;

int main()
{
  int t;
  cin >> t;
  while (t--)
  {
    int n, x;
    cin >> n;
    map<int, int> cnt;
    int answer = 0;
    for (int i = 0; i < n; ++i)
    {
      cin >> x;
      int target = (1LL << 31) - 1 ^ x;
      if (cnt.find(target) != cnt.end() && cnt[target] > 0)
      {
        answer += 1;
        cnt[target] -= 1;
        if (cnt[target] == 0)
        {
          cnt.erase(target); // Remove the entry if its count is 0 to keep the map clean
        }
      }
      else
      {
        cnt[x] += 1;
      }
    }
    int sum = 0;
    for (auto &pair : cnt)
    {
      sum += pair.second;
    }
    cout << answer + sum << endl;
  }
  return 0;
}