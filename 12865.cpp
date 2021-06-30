#include <cstdio>
#include <vector>
#include <algorithm>
#include <utility>
using namespace std;

void print(const vector<pair<int, int> > &v);

int main() {
	int n, k;
	int w, v;
	vector<pair<int, int> > items(1, make_pair(0, 0));
	scanf("%d%d", &n, &k);

	for (int i = 0; i < n; ++i) {
		scanf("%d%d", &w, &v);
		items.push_back(make_pair(w, v));
	}

	//print(items);
	vector<vector<int> > dp(n + 1, vector<int>(k + 1, 0));

	for (int i = 1; i <= n; ++i) {
		for (int j = 1; j <= k; ++j) {
			if (items[i].first > j) {
				dp[i][j] = dp[i - 1][j];
			} else {
				dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - items[i].first] + items[i].second);
			}
		}
	}

//	for (int i = 0; i <= n; ++i) {
//		for (int j = 0; j <= k; ++j) {
//			printf("%d, ", dp[i][j]);
//		}
//		printf("\n");
//	}

	printf("%d\n", dp[n][k]);

	return 0;
}

void print(const vector<pair<int, int> > &v) {
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		printf("w: %d, v: %d\n", itr->first, itr->second);
	}
}

