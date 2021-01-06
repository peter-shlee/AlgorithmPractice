#include <cstdio>
#include <vector>
#include <set>
#include <algorithm>
using namespace std;

void print(const vector<int> &v);
int get_index(const vector<int> &v, int t, int f, int e);

int main() {
	int n;
	int m;
	vector<int> nums;
	set<int> s;
	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		scanf("%d", &m);
		nums.push_back(m);
		s.insert(m);
	}

	vector<int> points(s.begin(), s.end());
//	print(points);
//	printf("%d\n", get_index(points, -9, 0, points.size()));

	for (auto itr = nums.begin(); itr != nums.end(); ++itr) {
		*itr = get_index(points, *itr, 0, points.size());
	}
	print(nums);

	return 0;
}

void print(const vector<int> &v) {
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		printf("%d ", *itr);
	}
	printf("\n");
}

int get_index(const vector<int> &v, int t, int f, int e) {
	int m = (f + e) / 2;
	if (v[m] == t) return m;

	if (f - e == 1) return -1;

	if (v[m] > t) return get_index(v, t, f, m);
	else return get_index(v, t, m + 1, e);
}
