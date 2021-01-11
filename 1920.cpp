#include <cstdio>
#include <unordered_set>
using namespace std;

int main() {
	int n, m;
	int temp;
	unordered_set<int> nums;

	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		scanf("%d", &temp);
		nums.insert(temp);
	}

	scanf("%d", &m);
	for (int i = 0; i < m; ++i) {
		scanf("%d", &temp);
		if (nums.find(temp) != nums.end()) {
			printf("1\n");
		} else {
			printf("0\n");
		}
	}

	return 0;
}
