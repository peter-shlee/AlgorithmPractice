#include <cstdio>
#include <vector>
#include <set>
using namespace std;

void print(vector<vector<int> > v);
int get_next_v(const vector<int> &answer, const set<int> &s);

int main() {
	int v, e, start;
	scanf("%d%d%d", &v, &e, &start);
	vector<vector<char> > g(v + 1, vector<char>(v + 1, 0)); // 인접 리스트로 수정해야 함 
	vector<int> answer(v + 1, 987654321);
	vector<bool> visited(v + 1, false);
	set<int> s;

	for (int i = 0; i < e; ++i) {
		int se, ee, l;
		scanf("%d%d%d", &se, &ee, &l);
		g[se][ee] = l;
	}
	//print(g);

	s.insert(start);
	visited[start] = true;
	answer[start] = 0;
	while (!s.empty()) {
		int cur_v = get_next_v(answer, s);
		s.erase(cur_v);

		for (int i = 1; i < g[cur_v].size(); ++i) {
			if (visited[i]) continue;
			if (g[cur_v][i]) {
				if (answer[cur_v] + g[cur_v][i] < answer[i]) {
					answer[i] = answer[cur_v] + g[cur_v][i];
					s.insert(i);
					visited[i] = true;
				}
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

int get_next_v(const vector<int> &answer, const set<int> &s) {
	int next_v;
	int min = 987654321;

	for (auto itr = s.begin(); itr != s.end(); ++itr) {
		if (answer[*itr] < min) {
			min = answer[*itr];
			next_v = *itr;
		}
	}

	return next_v;
}

void print(const vector<vector<int> > &v) {
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		for (auto itr2 = itr->begin(); itr2 != itr->end(); ++itr2) {
			printf("%d, ", *itr2);
		}
		printf("\n");
	}
}
