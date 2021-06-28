// 제곱수의 합
// https://www.acmicpc.net/problem/1699

#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

void print(vector<int> &v);

int main() {
	int n = 0;

	scanf("%d", &n);

	vector<int> dp = vector<int>(n + 1, 987654321);
	dp[0] = 0;
	dp[1] = 1;

	for (int i = 2; i <= n; ++i) {
		int s = int(sqrt(i));
		if (s * s == i) {
			dp[i] = 1;
			continue;
		}
		for (int j = 1; j <= s; ++j) {
			dp[i] = min(dp[i], dp[i - (j * j)] + 1);
		}
	}
	printf("%d\n", dp[n]);
	//print(dp);

	return 0;
}

void print(vector<int> &v) {
	for (int i = 0; i < v.size(); ++i) {
		printf("%d ", v[i]);
	}
	printf("\n");
}
