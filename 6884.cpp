// https://www.acmicpc.net/problem/6884
// 소수 부분 수열

#include <cstdio>
#include <vector>
#include <cmath>
using namespace std;

bool is_primary(int n);

int main() {
    int num_of_test_case;
    scanf("%d", &num_of_test_case);

    for (int i = 0; i < num_of_test_case; ++i){
        vector<int> dp = vector<int>(10001, 0);
		vector<int> num_seq;
		int seq_len;
		bool end_flag = false;
		scanf("%d", &seq_len);

		for (int j = 0; j < seq_len; ++j) {
			scanf("%d", &dp[j]);
			num_seq.push_back(dp[j]);
		}

		for (int n = 2; n <= seq_len; ++n) {
			for (int s = 0; s + n - 1 < seq_len; ++s) {
				dp[s] += num_seq[s + n - 1];
				if (is_primary(dp[s])) {
					end_flag = true;
					printf("Shortest primed subsequence is length %d:", n);
					for (int j = 0; j < n; ++j) {
						printf(" %d", num_seq[s + j]);
					}
					printf("\n");
					break;
				}
			}
			if (end_flag) break;
		}
		if (end_flag) continue;
		else printf("This sequence is anti-primed.\n");
    }

    return 0;
}

bool is_primary(int n) {
	if (n < 2) return false;

	for (int i = 2; i <= sqrt(n); ++i) {
		if (n % i == 0) return false;
	}

	return true;
}
