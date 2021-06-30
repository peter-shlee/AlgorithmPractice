#include <cstdio>
#include <vector>
using namespace std;

int main() {
	int n;
	int m;
	int max_cnt;
	int max_index;
	int answer = 0;
	int final_answer = 0;
	vector<int> numbers(7, 0);

	scanf("%d", &n);

	for (int i = 0; i < n; ++i) {
		max_index = 0;
		max_cnt = 0;
		answer = 0;

		for (auto itr = numbers.begin(); itr != numbers.end(); ++itr) {
			*itr = 0;
		}

		for (int j = 0; j < 3; ++j) {
			scanf("%d", &m);
			++numbers[m];
		}

		for (int j = 1; j <= 6; ++j) {
			if (max_cnt <= numbers[j]) {
				max_cnt = numbers[j];
				max_index = j;
			}
		}

		if (max_cnt >= 3) {
			answer = 10000 + max_index * 1000;
		} else if (max_cnt >= 2) {
			answer = 1000 + max_index * 100;
		} else {
			answer = max_index * 100;
		}

		if (final_answer < answer) {
			final_answer = answer;
		}
	}
	printf("%d\n", final_answer);

	return 0;
}
