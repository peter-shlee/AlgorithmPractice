// 1로 만들기
// https://www.acmicpc.net/problem/1463

#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int n = 0;
	scanf("%d", &n);

	vector<int> dp = vector<int>(n + 1, 987654321);
	dp[n] = 0;

	for (int i = n; i > 1; --i) {
		int count = dp[i] + 1;
		if (i % 3 == 0) {
			if (dp[i / 3] > count) {
				dp[i / 3] = count;
			}
		}

		if (i % 2 == 0) {
			if (dp[i / 2] > count) {
				dp[i / 2] = count;
			}
		}

		if (dp[i - 1] > count) {
			dp[i - 1] = count;
		}
		
	}

	printf("%d\n", dp[1]);

	return 0;
}
