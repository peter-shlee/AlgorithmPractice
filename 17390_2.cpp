// https://www.acmicpc.net/problem/17390
// 이건 꼭 풀어야 해!

#include <cstdio>
#include <vector>
#include <queue>
#include <algorithm>
using namespace std;

int main() {
	int n = 0;
	int q = 0;
	int next_number = 0;
	int s = 0;
	int e = 0;
	priority_queue<int, vector<int>, greater<int> > pq;
	vector<int> p_sum;

	scanf("%d%d", &n, &q);

	for (int i = 0; i < n; ++i) {
		scanf("%d", &next_number);
		pq.push(next_number);
	}

	p_sum.push_back(0);
	for (int i = 1; i <= n; ++i) {
		p_sum.push_back(p_sum[i - 1] + pq.top());
		pq.pop();
	}

	for (int i = 0; i < q; ++i) {
		scanf("%d%d", &s, &e);
		printf("%d\n", p_sum[e] - p_sum[s - 1]);
	}

	return 0;
}
