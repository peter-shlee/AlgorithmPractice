#include <cstdio>
#include <cstdlib>
#include <set>
#include <vector>
#include <algorithm>
using namespace std;

int getGCD(int a, int b);

int main() {
	int t, n, i, j, k;
	int new_num;
	multiset<int> *GCDs;
	vector<int> *nums;

	scanf("%d", &t);
	for (i = 0; i < t; ++i) {
		long long sum = 0;
		scanf("%d", &n);
		nums = new vector<int>();
		GCDs = new multiset<int>();

		for (j = 0; j < n; ++j) {
			scanf("%d", &new_num);
			nums->push_back(new_num);
		}
		sort(nums->begin(), nums->end());

		for (j = 0; j < n; ++j) {
			for (k = j + 1; k < n; ++k) {
				GCDs->insert(getGCD((*nums)[j], (*nums)[k]));
			}
		}

		for (set<int>::iterator it = GCDs->begin(); it != GCDs->end(); ++it) {
			sum += *it;
		}

		printf("%ld\n", sum);

		delete GCDs;
		delete nums;
	}



	return 0;
}

int getGCD(int a, int b) {
	while (b > 0) {
		int tmp = b;
		b = a % b;
		a = tmp;
	}

	return a;
}
