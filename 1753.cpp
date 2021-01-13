#include <cstdio>
#include <vector>
#include <set>
#include <utility>
#include <queue>
using namespace std;

void print(const vector<vector<pair<int, char> > > &v);

struct compare{
	bool operator()(const pair<int, int> &a, const pair<int, int> &b) {
		return a.second > b.second;
	}
};

int main() {
	int v, e, start;
	scanf("%d%d%d", &v, &e, &start);
	vector<vector<pair<int, char> > > g(v + 1);
	vector<int> answer(v + 1, 987654321);
	vector<bool> visited(v + 1, false);
	priority_queue<pair<int, int>, vector<pair<int, int> >, compare> q;

	for (int i = 0; i < e; ++i) {
		int se, ee, l;
		scanf("%d%d%d", &se, &ee, &l);
		g[se].push_back(make_pair(ee, l));
	}
	//print(g);

	q.push(make_pair(start, 0));
	answer[start] = 0;
	while (!q.empty()) {
		int cur_v = q.top().first;
		q.pop();
		if (visited[cur_v]) {
			continue;
		} else {
			visited[cur_v] = true;
		}

		for (int i = 0; i < g[cur_v].size(); ++i) {
			if (answer[cur_v] + g[cur_v][i].second < answer[g[cur_v][i].first]) {
				answer[g[cur_v][i].first] = answer[cur_v] + g[cur_v][i].second;
				q.push(make_pair(g[cur_v][i].first, answer[g[cur_v][i].first]));
			}
		}
	}

	for (int i = 1; i < answer.size(); ++i) {
		if (answer[i] == 987654321) {
			printf("INF\n");
		} else {
			printf("%d\n", answer[i]);
		}
	}


	return 0;
}

void print(const vector<vector<pair<int, char> > > &v) {
	int i = 1;
	for (auto itr = v.begin() + 1; itr != v.end(); ++itr) {
		printf("%d: ", i++);
		for (auto itr2 = itr->begin(); itr2 != itr->end(); ++itr2) {
			printf("i:%d value:%d, ", itr2->first, itr2->second);
		}
		printf("\n");
	}
}
