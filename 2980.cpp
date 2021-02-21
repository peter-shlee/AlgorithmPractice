// https://www.acmicpc.net/problem/2980
// 도로와 신호등

#include <cstdio>
#include <vector>
#include <utility>
using namespace std;

int main() {
	int N, L, D, R, G;
	vector<int> position;
	vector<pair<int, int> > time;

	scanf("%d%d", &N, &L);

	for (int i = 0; i < N; ++i) {
		scanf("%d%d%d", &D, &R, &G);
		position.push_back(D);
		time.push_back(make_pair(R, G));
	}

	int current_time = 0;
	int prev_position = 0;
	for (int i = 0; i < position.size(); ++i) {
		current_time += position[i] - prev_position;
		prev_position = position[i];

		int traffic_remain_time = current_time % (time[i].first + time[i].second);
		if (traffic_remain_time  < time[i].first) {
			current_time += time[i].first - traffic_remain_time;
		}
	}
	current_time += L - position[position.size() - 1];

	printf("%d\n", current_time);

	return 0;
}
