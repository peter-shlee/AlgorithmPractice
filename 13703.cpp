#include <cstdio>
#include <cmath>
#include <vector>
using namespace std;

int dfs(int current_time, const int end_time, int current_depth, vector<vector<int> > &dp)
{
	if (current_depth == 0)
	{
		return 1;
	}

	if (current_time == end_time)
	{
		return 0;
	}

	if (dp[64 + current_depth + 1][current_time + 1] == -1) {
		 dp[64 + current_depth + 1][current_time + 1] = 
			 dfs(current_time + 1, end_time, current_depth + 1, dp);
	}

	if (dp[64 + current_depth - 1][current_time + 1] == -1) {
		dp[64 + current_depth - 1][current_time + 1] = 
			dfs(current_time + 1, end_time, current_depth - 1, dp);
	}

	if (dp[64 + current_depth + 1][current_time + 1] == 1 && dp[64 + current_depth - 1][current_time + 1] == 1) {
		return 1;
	}

	return 2;
}

long long check_count(int current_time, const int end_time, int current_depth, vector<vector<int> > &dp) {
	if (dp[64 + current_depth][current_time] == 1) {
		return pow(2, end_time - current_time);
	} else if (dp[64 + current_depth][current_time] == 0) {
		return 0;
	}

	return check_count(current_time + 1, end_time, current_depth + 1, dp) + check_count(current_time + 1, end_time, current_depth - 1, dp);
}

int main()
{
	int n = 0, k = 0;
	long long eaten_count = 0;
	vector<vector<int> > dp(150, vector<int>(70, -1));
	scanf("%d%d", &k, &n);

	dfs(0, n, k, dp);
	eaten_count = check_count(0, n, k, dp);
	printf("%lld\n", (long long)pow(2, n) - eaten_count);

	return 0;
}
