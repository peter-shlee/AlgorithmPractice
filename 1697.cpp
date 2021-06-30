#include <cstdio>
#include <set>
#include <queue>
#include <cmath>
using namespace std;

int main() {
	int N, K;
	int answer = 0;
	queue<pair<int, int> > q;
	set<int> visited;
	scanf("%d%d", &N, &K);

	q.push(make_pair(N, 0));
	while (!q.empty()) {
		int cur_pos = q.front().first;
		int cnt = q.front().second;
		q.pop();

		if (cur_pos == K) {
			answer = cnt;
			break;
		}
		
		if (cur_pos > 0) {
			if (visited.find(cur_pos - 1) == visited.end()) {
				if (cur_pos - 1 == K) {
					answer = cnt + 1;
					break;
				}
				visited.insert(cur_pos - 1);
				q.push(make_pair(cur_pos - 1, cnt + 1));
			}
		}
		
		if (visited.find(cur_pos + 1) == visited.end()) {
			if (cur_pos + 1 == K) {
					answer = cnt + 1;
					break;
			}
			visited.insert(cur_pos + 1);
			q.push(make_pair(cur_pos + 1, cnt + 1));
		}
		
		if (cur_pos * 2 <= K || (2 * cur_pos > K && cur_pos * 2 - K < abs(K - cur_pos) - 1)) {
			if (visited.find(cur_pos * 2) == visited.end()) {
				if (cur_pos * 2 == K) {
						answer = cnt + 1;
						break;
				}
				visited.insert(cur_pos * 2);
				q.push(make_pair(cur_pos * 2, cnt + 1));
			}
		}
	}

	printf("%d\n", answer);

	return 0;
}
