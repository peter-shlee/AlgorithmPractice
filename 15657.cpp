#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

bool find(const vector<int> &v, int n);
void make(vector<int> v, int i);
void print(const vector<int> &v);

vector<int> nums;
int n, m;

int main() {
	scanf("%d%d", &n, &m);

	for (int i = 0; i < n; ++i) {
		int num;
		scanf("%d", &num);
		nums.push_back(num);
	}
	sort(nums.begin(), nums.end());

	make({}, 0);

	return 0;
}

void make(vector<int> v, int i) {
	if (v.size() == m) {
		print(v);
		return;
	}

	for (; i < nums.size(); ++i) {
		v.push_back(nums[i]);
		make(v, i);
		v.pop_back();
	}
}

void print(const vector<int> &v) {
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		printf("%d ", *itr);
	}
	printf("\n");
}

bool find(const vector<int> &v, int n) {
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		if (*itr == n) return true;
	}
	return false;
}
