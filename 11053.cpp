#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

bool can_merge(const vector<int> &a, const vector<int> &b);
vector<int> merge_vector(const vector<int> &a, const vector<int> &b);
vector<int> &get_large_vector(vector<int> &a, vector<int> &b);

void print_3_dim_vector(const vector<vector<vector<int> > > &v);
void print_2_dim_vector(const vector<vector<int> > &v);
void print_vector(const vector<int> &v);

int main() {
	int n, a;
	scanf("%d", &n);
	vector<int> nums(n);
	vector<vector<vector<int> > > dp(n, vector<vector<int> >(n));

	for (int i = 0; i < n; ++i) {
		scanf("%d", &a);
		nums[i] = a;
		dp[i][i].push_back(a);
	}

	for (int i = 1; i < n; ++i) {
		for (int j = 0; j + i < n; ++j) {
			for (int k = j; k < j + i; ++k) {
				if (can_merge(dp[j][k], dp[k + 1][j + i])) {
					vector<int> merged_vector = merge_vector(dp[j][k], dp[k + 1][j + i]);
					dp[j][j + i] = get_large_vector(merged_vector, dp[j][j + i]);
				} else {
					vector<int> large_vector = get_large_vector(dp[j][k], dp[k + 1][j + i]);
					dp[j][j + i] = get_large_vector(large_vector, dp[j][j + i]);
				}
			}
		}
	}

	//print_3_dim_vector(dp);
	printf("%lu\n", dp[0][n - 1].size());

	return 0;
}

bool can_merge(const vector<int> &a, const vector<int> &b) {
	return a[a.size() - 1] < b[0];
}

vector<int> merge_vector(const vector<int> &a, const vector<int> &b) {
	vector<int> merged_vector(a.size() + b.size());
	merge(a.begin(), a.end(), b.begin(), b.end(), merged_vector.begin());

	return merged_vector;
}

vector<int> &get_large_vector(vector<int> &a, vector<int> &b) {
	if (a.size() > b.size()) {
		return a;
	} else if (a.size() < b.size()) {
		return b;
	} else {
		if (a[a.size() - 1] < b[b.size() - 1]) {
			return a;
		} else {
			return b;
		}
	}
}

void print_3_dim_vector(const vector<vector<vector<int> > > &v) {
	printf("\n");
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		print_2_dim_vector(*itr);
	}
}

void print_2_dim_vector(const vector<vector<int> > &v) {
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		print_vector(*itr);
	}
	printf("\n");
}

void print_vector(const vector<int> &v) {
	printf("[");
	for (int i = 0; i < v.size(); ++i) {
		printf("%d, ", v[i]);
	}
	printf("],\t\t\t");
}
