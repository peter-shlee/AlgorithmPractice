// 오르막 수
// https://www.acmicpc.net/problem/11057

#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int n = 0;
	scanf("%d", &n);

	vector<vector<int> > dp = 
		vector<vector<int> >(10, vector<int>(n + 1, 0));

	for (int i = 0; i < 10; ++i) {
		dp[i][1] = 1;
		dp[i][0] = 0;
	}

	for (int i = 2; i <= n; ++i) {
		dp[0][i] = 1;
	}

	for (int i = 2; i <= n; ++i) {
		for (int j = 1; j < 10; ++j) {
			for (int k = 0; k <= j; ++k) {
				dp[j][i] = (dp[j][i] + dp[k][i - 1]) % 10007;
			}
		}
	}

	int answer = 0;
	for (int i = 0; i < 10; ++i) {
		answer = (answer + dp[i][n]) % 10007;
	}
	printf("%d\n", answer);

	return 0;
}
