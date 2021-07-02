// 영역 구하기
// https://www.acmicpc.net/problem/2583

#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;

void print_graph(vector<vector<int> > &graph);
int dfs(vector<vector<int> > &graph, int r, int c, int count);
bool is_valid_index(vector<vector<int> > &graph, int r, int c);
void print_vector(vector<int> &v);

int adjacent_indices[4][2] = {{1, 0}, {-1, 0}, {0, 1}, {0, -1}};

int main() {
	int m, n, k;

	scanf("%d%d%d", &m, &n, &k);
	vector<vector<int> > graph = vector<vector<int> >(m, vector<int>(n, 0));
	for (int i = 0; i < k; ++i) {
		int i1, i2, j1, j2;
		scanf("%d%d%d%d", &j1, &i1, &j2, &i2);

		for (int r = i1; r < i2; ++r) {
			for (int c = j1; c < j2; ++c) {
				graph[r][c] = 1;
			}
		}
	}

	int answer = 0;
	vector<int> counts = vector<int>();
	for (int r = 0; r < m; ++r) {
		for (int c = 0; c < n; ++c) {
			if (graph[r][c] == 0) {
				answer += 1;
				counts.push_back(dfs(graph, r, c, 0));
			}
		}
	}
	printf("%d\n", answer);
	sort(counts.begin(), counts.end());
	print_vector(counts);
	//print_graph(graph);

	return 0;
}

void print_vector(vector<int> &v) {
	for (auto itr = v.begin(); itr != v.end(); ++itr) {
		printf("%d ", *itr);
	}
	printf("\n");
}

int dfs(vector<vector<int> > &graph, int r, int c, int count) {
	graph[r][c] = 1;
	count += 1;

	for (int i = 0; i < 4; ++i) {
		int next_r = r + adjacent_indices[i][0];
		int next_c = c + adjacent_indices[i][1];

		if (is_valid_index(graph, next_r, next_c)) {
			if (graph[next_r][next_c] == 0) {
				count = dfs(graph, next_r, next_c, count);
			}
		}
	}	

	return count;
}

bool is_valid_index(vector<vector<int> > &graph, int r, int c) {
	if (r < 0 || c < 0) {
		return false;
	}

	if (r >= graph.size()) {
		return false;
	}

	if (c >= graph[r].size()) {
		return false;
	}

	return true;
}

void print_graph(vector<vector<int> > &graph) {
	for (auto itr = graph.begin(); itr != graph.end(); ++itr) {
		for (auto itr2 = (*itr).begin(); itr2 != (*itr).end(); ++itr2) {
			printf("%d ", *itr2);
		}
		printf("\n");
	}

	return;
}
