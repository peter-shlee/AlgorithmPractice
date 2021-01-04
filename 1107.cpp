#include <cstdio>
#include <set>
#include <string>
#include <algorithm>
using namespace std;

int main() {
	set<int> broken_num;
	int N;
	int M;
	int answer = 0;
	string target_str;
	scanf("%d", &N);
	scanf("%d", &M);

	for (int i = 0; i <= 9; ++i) {
		broken_num.insert(i);
	}

	for (int i = 0; i < M; ++i) {
		int num;
		scanf("%d", &num);
		broken_num.erase(num);
	}

	target_str = to_string(N);

	for (auto itr = target_str.begin(); itr != target_str.end(); ++itr) {
		int min_cnt = 10;
		char min_num = *itr;
		for (auto set_itr = broken_num.begin(); set_itr != broken_num.end(); ++set_itr) {
			int dif = abs(*itr - (*set_itr + '0'));
			if (dif < min_cnt) {
				min_cnt = dif;
				min_num = *set_itr + '0';
			}
		}
		*itr = min_num;
	}
	if (broken_num.empty())
		target_str = to_string(100);

	//printf("m:%d\n", stoi(target_str));
	answer = target_str.length();
	answer += abs(stoi(target_str) - N);

	if (!broken_num.empty()) {
		int l = 0, g = 0;
		int max_av = 0;
		int min_av = 9;
		for (auto itr = broken_num.begin(); itr != broken_num.end(); ++itr) {
			max_av = max(max_av, *itr);
			min_av = min(min_av, *itr);
		}

		//printf("%d, %d\n", max_av, min_av);
		string tmp = "0";
		for (int i = 1; i < target_str.length(); ++i) {
			tmp += to_string(max_av);
		}
		//printf("%d\n", stoi(tmp));
		answer = min(answer, N - stoi(tmp));

		tmp = "0";
		for (int i = 1; i <= target_str.length() + 1; ++i) {
			tmp += to_string(min_av);
		}
		//printf("%d\n", stoi(tmp));
		if (stoi(tmp) != 0)
			answer = min(answer, stoi(tmp) - N);
	}

	answer = min(answer, abs(N - 100));
	printf("%d\n", answer);

	return 0;
}
